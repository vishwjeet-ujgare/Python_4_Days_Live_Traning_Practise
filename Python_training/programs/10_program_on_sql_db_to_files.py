"""
Get data from database
then
write to files 'db_dump_1.txt', 'db_dump_2.csv'
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


print("# Task-2: Create Empty files 'db_dump_1.txt' and 'db_dump_2.csv' with heading")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_txt_file_handle = open("db_dump_1.txt", "w")
my_csv_file_handle = open("db_dump_2.csv", "w")

# Step-2: Write Heading
# --------------------
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)


# Step-3: Disconnect
# --------------------
# We will close at the end

print("""
Files db_dump_1.txt and db_dump_2.csv
created with header, please check
""")

print("#"*40, end="\n\n")
####################################

print("Write to files")
print("-"*20)
# --------------------
# my_db_result=[(ip,dt,img,url),(ip,dt,img,url), (ip,dt,img,url)]
for i, j, k, l in my_db_result:
    print(i, j, k, l, sep="\t", file=my_txt_file_handle, flush=True)
    print(i, j, k, l, sep=",", file=my_csv_file_handle, flush=True)

print("#"*40, end="\n\n")
####################################

print("""
Files db_dump_1.txt and db_dump_2.csv
created with db data, please check
""")
