"""
Get data from web, extract info
then
send extracted info to sql database
"""

'''
How to communicate with databases?

python program  <--Communicate using library--> Any Databases(SQL/No-SQL)

Example:
python program  <--Communicate using library "cx_Oracle"--> oracle Databases
python program  <--Communicate using library "mysql.connector"--> mysql Databases
python program  <--Communicate using library "sqlite3"--> SQLite Databases
'''

'''
We need database?
- We can use SQLIte database
'''

'''
How to communicate with SQLIte database
OPTION-1: Using SQLite database software we can communicate
OR
OPTION-2: Using python library sqlite3 also we can create/communicate with sqlite database
'''

# --------------------
# Split into smaller
# --------------------
# Task-1: Get data from website using urllib-Keep it in variable
# Task-2: Extract log data using beautifulsoup
# Task-3: Create database and table - keep it ready
# Task-4: Extract info and send extracted info to database
# --------------------

print("# Task-1: Get data from website using urllib-Keep it in variable")
print("-"*20)
# --------------------

import urllib.request as ur

# Step-1: Connect
# --------------------
my_web_file_handle = ur.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

# Step-2: Read
# --------------------
web_content = my_web_file_handle.read()

# Step-3: Disconnect
# --------------------
my_web_file_handle.close()

web_content = web_content.decode()
print(web_content)

print("#"*40, end="\n\n")
####################################

print("# Task-2: Extract info using beautifulsoup")
print("-"*20)
# --------------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
log_data = soup.body.pre.text
list_of_lines = log_data.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
####################################

print("# Task-3: Create database and table - keep it ready")
print("-"*20)
# --------------------

import sqlite3

print("Create/Connect to database 'my_data_db.sqlite'")
my_db_connection = sqlite3.connect('my_data_db.sqlite')
print("Done")

print("Get the cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done")

print("Create table if not present")
my_query = '''
CREATE TABLE IF NOT EXISTS MY_DATA_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
'''
my_db_cursor.execute(my_query)
print("Done")

print("#"*40, end="\n\n")
####################################

print("Extract IP, DATE, PICS, URL")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[0-9a-zA-Z./_]+).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        my_query = f"INSERT INTO MY_DATA_TABLE VALUES('{ip}', '{dt}', '{img}', '{url}')"
        print("Executing:", my_query)
        my_db_cursor.execute(my_query)
        print("one record inserted", end="\n\n")

my_db_connection.commit()
print("All records inserted. Please check database", end="\n\n")
my_db_connection.close()
print("DB connection closed")

print("#"*40, end="\n\n")
####################################
