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
import sqlite3
from pprint import pprint
import sqlite3
import re
import os
import urllib
import json
import datetime
from PIL import Image
import requests
import webbrowser

#captures time of download for data logging
time_now = datetime.datetime.now()

#SQL Part of code
myConnection = sqlite3.connect('social_network.db')
myCursor = myConnection.cursor()

ApodApi = client.HTTPSConnection('api.nasa.gov', 443)

ApodApiKey = ""

ApodApi.request('GET', '/planetary/apod?api_key=e7K9LCLA1dSndstU85ceydJDPiwRHkEOtCfV0aqQ')

response = ApodApi.getresponse()

ApodData = response.read().decode()

define = json.loads(ApodData)

#Format the sql into text to be used for string related code
explanation = "{0}".format(define['explanation'])
hdurl = "{0}".format(define.get('hdurl', 'N/A'))
title = "{0}".format(define['title'])
media_type = "{0}".format(define['media_type'])
url = "{0}".format(define['url'])

addApodQuery = """INSERT INTO apod(
explanation,
media_type,
title,
hdurl,
url)
VALUES (?,?,?,?,?);"""

myApod = (
explanation,
media_type,
title,
hdurl,
url
)
try:
    image_name = re.search(r"((\w*[-]?\w*).jpg$)", hdurl)
    found_name = image_name.group(2)
except AttributeError:
    print("Continue")


#creating a function called download_image
def download_image(response):
    if os.path.isfile(f'{found_name}.png') == False:
        raw_image = requests.get(hdurl).content
        with open(f'{found_name}.jpg', 'wb') as file:
            file.write(raw_image)
            
    else:
        return FileExistsError
        

myCursor.execute(addApodQuery, myApod)
#This allows for only distinct query to be capture, i.e. no duplicants
myCursor.execute("SELECT DISTINCT explanation, media_type, title, hdurl, url FROM apod")

myConnection.commit()
myConnection.close()
#end of sql code

#path is where the image is located
try:
    Path = '.\\' + image_name.group(1)
except AttributeError:
    print ("No path to image.")
 

if (media_type == 'video'):
    print ("Today's image of the day is actually a youtube video and won't be uploaded to your computer background. Enjoy the video!!!")
    webbrowser.open(url)
elif (os.path.exists(Path) == True):
    print ("The Image of the day is already been downloaded")
else:
    #Downloads actual image
    download = download_image(response)
    #Gets size of image in bytes
    size_image = os.path.getsize(Path)

    
    #creates the database file to keep track of all logs inside txt file for better readings
    SQLite = open("Download_Log.txt", "a")
    SQLite.write("Image of the day downloaded at " + time_now.strftime("%Y-%m-%d %I:%M%p") + " Size of file is " + str(size_image) + " Bytes.\n")
    SQLite.write("File name is: " + image_name.group(1) + "\n")
    SQLite.close()
SQLite = open("Download_Log.txt", "r")
print (SQLite.read())
SQLite.close()

Fix_it_Regex = re.match(r"((?:.*\.))", explanation)

print (title + ", is the image of the day.\nHere are some cool facts about the image:\n" + Fix_it_Regex.group(1))

    
