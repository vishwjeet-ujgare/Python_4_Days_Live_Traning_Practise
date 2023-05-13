"""
Get data from database
and
produce
db_dump_3.txt
db_dump_4.csv
db_dump_5.xlsx
db_dump_6.json
"""

# -----------
# Split into smaller tasks
# -----------
# Task-1: Get data from database
# Task-2: Write to files
# -----------

print("# Task-1: Get data from database")
print("-"*20)
# --------------------

import sqlite3

print("Create/Connect to database 'my_data_db.sqlite'")
my_db_connection = sqlite3.connect('my_data_db.sqlite')
print("Done")

print("Get the cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done")

my_query = "SELECT * FROM MY_DATA_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
print(my_db_result)

print("#"*40, end="\n\n")
####################################

print("Create dataframe with db data")
print("-"*20)
# --------------------
import pandas as pd
my_db_data_df = pd.DataFrame(my_db_result,columns=["IP", "DATE", "PICS", "URL"])
print(my_db_data_df)

print("#"*40, end="\n\n")
####################################

print("Write to files")
print("-"*20)
# --------------------

my_db_data_df.to_csv("db_dump_3.txt", sep="\t")
my_db_data_df.to_csv("db_dump_4.csv") # default sep=","
my_db_data_df.to_excel("db_dump_5.xlsx")
to_json_file_df = my_db_data_df.T # Transpose, make rows to columns/columns to rows
print(to_json_file_df)
to_json_file_df.to_json("db_dump_6.json")

print("""
Files,
db_dump_3.txt
db_dump_4.csv
db_dump_5.xlsx
db_dump_6.json
created. Please check
""")
print("#"*40, end="\n\n")
####################################
