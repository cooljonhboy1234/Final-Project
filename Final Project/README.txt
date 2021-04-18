FINAL PROJECT

Creator: Jonnathan Raskin
Student ID: 10244797

This folder is to be used for capturing API data from the NASA's API for the image of the day.

All updates, notes and logs will be posted in github.

Link to github: https://github.com/cooljonhboy1234/Final-Project

if you get an error with the import request it just means you don't have that module installed.

Solution:

pip3 install requests

that should do the trick and the script should work!

Please note:

In the RUN_THIS.ps1

where $PathTo, change the path to were the script is placed on you computer.

Example.
$PathTo = Join-Path -Path 'C:\change\this\to\file\location\cache' -ChildPath $NewestImage