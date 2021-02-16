# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:20:19 2021

@author: dl
"""

import sqlite3
from sqlite3 import Error

#-----Setup SQL Database and Entries-----
def create_connection(path):

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        
connection = create_connection("key_app.sqlite")

#-----Create SQL Data-----
create_table_key_1month = """
CREATE TABLE IF NOT EXISTS key_1month (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT,
  activated INTEGER,
  time_activation timestamp
);
"""

from datetime import date
today = date.today()

create_key_1month = """
INSERT INTO
  key_1month (key, activated, time_activation)
VALUES
  ('1234567890', 0, 'today');
"""

execute_query(connection, create_table_key_1month)  
execute_query(connection, create_key_1month)   

# insert developer detail
sqlite_insert_with_param = """INSERT INTO 'key_1month'
                  (key, activated, time_activation) 
                  VALUES (?, ?, ?);"""

data_tuple = ('1234567890', 0, today)
cursor = connection.cursor()
cursor.execute(sqlite_insert_with_param, data_tuple)
connection.commit()


select_key_1month = "SELECT * from key_1month"
users = execute_read_query(connection, select_key_1month)

for user in users:
    print(user)


    
