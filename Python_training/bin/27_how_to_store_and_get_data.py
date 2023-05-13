"""
How to store the data inside the objects
and also how to get the data from object

1-way to store/get

Here we will come to know about,
1) CLASS VARIABLES
2) INSTANCE VARIABLES
"""

class Employee:
    pass

# Create 2 objects
e1 = Employee()
e2 = Employee()

# -----------------
# Store the values in all 2 objects
# -----------------
Employee.company_name = "XYZ Company"
# Inside 'Employee' object, it will create varoiable 'company_name'
# and store the value "XYZ Company"
e1.name = "emp-1"
# Inside 'e1' object, it will create variable 'name'
# and store the value "emp-1"
e2.name = "emp-2"
# Inside 'e2' object, it will create variable 'name'
# and store the value "emp-2"
# -----------------

# -----------------
# Access values
# -----------------
print("company Name:", Employee.company_name)
print("emp-1 name:", e1.name)
print("emp-2 name:", e2.name)
# -----------------


# -----------------
# What is there inside objects
# -----------------
print("\n\n")
print("Inside 'Employee' object:", dir(Employee), sep="\n", end="\n\n")
print("Inside 'e1' object:", dir(e1), sep="\n", end="\n\n")
print("Inside 'e2' object:", dir(e2), sep="\n", end="\n\n")
# -----------------

# -----------------
# Example: I need to store single database details
# -----------------

# 1-way # Storing in global scope
host='192.168.1.10'
port=1234
username="abc"
pasword="xyz"
db="mydb"

# 2-way # storing inside object
class dbDetails:
    pass

dbDetails.host='192.168.1.10'
dbDetails.port=1234
dbDetails.username="abc"
dbDetails.pasword="xyz"
dbDetails.db="mydb"
# -----------------

# -----------------
# Example: I need to store 2 database details
# -----------------

# 1-way # Storing in global scope
host_1='192.168.1.10'
port_1=1234
username_1="abc"
pasword_1="xyz"
db_1="mydb"

host_2='192.168.1.11'
port_2=1234
username_2="abc"
pasword_2="xyz"
db_2="mydb"

# 2-way # storing inside object
class dbDetails:
    pass

db1 = dbDetails()
db2 = dbDetails()

db1.host='192.168.1.10'
db1.port=1234
db1.username="abc"
db1.pasword="xyz"
db1.db="mydb"

db2.host='192.168.1.11'
db2.port=1234
db2.username="abc"
db2.pasword="xyz"
db2.db="mydb"

# -----------------
