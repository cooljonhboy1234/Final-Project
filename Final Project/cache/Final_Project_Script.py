#.-- .... -.-- / ..- / -- .- -.- . / -- . / -.-. --- -- -- . -. -
# Description:
#   Will capture the image of the day from nasa's data base
#   and change the background to the new images everyday. 
#
# Usage: Final_Project_Script.py
#   
#
#    
#.-- .... -.-- / ..- / -- .- -.- . / -- . / -.-. --- -- -- . -. -
from http import client
import re
import os
import urllib
import json
import datetime
#since these modules exists outside of python i need to append them to the sys
import sys
sys.path.append(r'\Users\jonna\apod-api\lib')
sys.path.append(r'\Users\jonna\apod-api\apod_parser')
import apod_object_parser




#gives api key to nasa's data base to allow capturing of data
response = apod_object_parser.get_data('e7K9LCLA1dSndstU85ceydJDPiwRHkEOtCfV0aqQ')

#captures date of image posted
date = apod_object_parser.get_date(response)

#captures time of download for data logging
time_now = datetime.datetime.now()

Path = 'C:/Users/jonna/OneDrive/Desktop/scripting APP/Final Project/cache/' + date + '.jpg'


#captures actual image url
url = apod_object_parser.get_hdurl(response)

if (os.path.exists(Path) == True):
    print ("The Image of the day is already been downloaded")
else:
    #Downloads actual image
    download_image = apod_object_parser.download_image(url, date)
    size_image = os.path.getsize(Path)
    
    #creates the database file to keep track of all logs
    SQLite = open("SQLite_Database.txt", "a")
    SQLite.write("Image of the day downloaded at " + str(time_now) + " Size of file is " + str(size_image) + " Bytes.\n")
    SQLite.write("File name is: " + date + ".jpg\n")
    SQLite.close()
SQLite = open("SQLite_Database.txt", "r")
print (SQLite.read())
SQLite.close()

#after everything is done can choose wether to add to the log or not.
print ("Would you like to add to the log.txt of your work today? (Y/N) ")
log_it = input().upper()

#This will pre count the logs, so it knows what log number comes next
Logging = open("Log.txt", "r")
num_Check = len(re.findall("Log \d*", Logging.read()))
Log_num = str(num_Check + 1)
Logging.close()

if (log_it == "Y"):

    print ("\nTell me what you did? ")
    user_input = input()
   
    Logging = open("Log.txt", "a")   
    Logging.write(time_now.strftime("\n%Y-%m-%d %I:%M%p Log " + str(Log_num) + ": \n" + user_input))
    Logging.close()
else:
    print("Goodbye!")
    
