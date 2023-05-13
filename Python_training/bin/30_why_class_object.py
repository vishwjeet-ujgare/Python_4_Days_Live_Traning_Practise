"""
Why class object?
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
e1.name = "emp-1"
e2.name = "emp-2"
# -----------------

# -----------------
# print company_name
# -----------------
print("Accessing Company Name using CLASS object 'Employee': ", Employee.company_name)
print("Accessing Company Name using INSTANCE object 'e1': ", e1.company_name)
print("Accessing Company Name using INSTANCE object 'e2': ", e2.company_name)
# -----------------

# -----------------
# CLASS OBJECT
# -----------------
# - CLASS OBJECT is common space for all instance objects
# - So, we can use CLASS OBJECT to store data which is common across all INSTANCE OBJECT
# - In above example, we assumed company_name is common for all instance
#   so, instead of storing in all instance object, we are storing inside class object
# - so, one copy only we are keeping - We are saving memory
# -----------------
