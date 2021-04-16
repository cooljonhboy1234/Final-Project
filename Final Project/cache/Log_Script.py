import re
import datetime

time_now = datetime.datetime.now()
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
    Logging.write(time_now.strftime("%Y-%m-%d %I:%M%p Log " + str(Log_num) + ": \n" + user_input + "\n\n"))
    Logging.close()
else:
    print("Goodbye!")