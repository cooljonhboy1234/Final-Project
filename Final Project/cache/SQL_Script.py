#Making datebase file
import sqlite3

myConnection = sqlite3.connect('social_network.db')
myCursor = myConnection.cursor()

createApodTable = """ CREATE TABLE IF NOT EXISTS apod (
id integer PRIMARY KEY,
explanation text NOT NULL,
media_type text NOT NULL,
title text NOT NULL,
url text NOT NULL,
hdurl image NOT NULL
);"""
myCursor.execute(createApodTable)
myConnection.commit()
myConnection.close()