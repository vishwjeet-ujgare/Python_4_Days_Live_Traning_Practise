"""
3rd way to store and get data

Here we will come to know about
1) Constructor : __new__
2) Initializer: __init__
"""


class Employee:
    company_name = "XYZ Company"

    def __init__(self, name):
        self.name = name

    def get_emp_name(self):
        # All logic to get data in db/file etc will come here
        return self.name

    @classmethod
    def get_company_name(cls):
        # All logic to get data in db/file etc will come here
        return cls.company_name


# Create 2 objects
e1 = Employee("emp-1")
e2 = Employee("emp-2")

# -----------------
# print values
# -----------------
print("comapny name:", Employee.get_company_name())
# object 'Employee' will automatically pass as 1st argument

print("Emp - 1 Name:", e1.get_emp_name())
# object 'e1' will go as 1st argument

print("Emp - 2 Name:", e2.get_emp_name())
# object 'e2' will go as 1st argument

# -----------------


# -----------------
# About 'object' class
# -----------------
# - 'object' is one class
# - there are many methods inside 'object' class
# - 2 of them are
#   1) __new__()
#   2) __init__()
# - __new__ method has logic to construct the object in memory
#   and __init__ is empty
# -----------------


# -----------------
# Classes are inhertited from 'object' class by default
# -----------------
# - if we create our own class like 'Employee',
#   by default internally linked to 'object' class
#   called INHERITED FROM object class by default
# - our class will be able to access methods present inside 'object'
# - when we create object of our class
#   like e1=Employee()
#   internally it will
#  automatically call __new__ to construct the object
#   after that automatically call __init__ to initialize the object
#  - We can also have __new__ & __init__ in our class
#       in that case, our class __new__ & __init__ will get executed
# - As of now, we have only __init__ in our class, so
#   __new__ will be executed from 'object' class
#   then
#   __init__ will ge executed from our class
# -----------------

