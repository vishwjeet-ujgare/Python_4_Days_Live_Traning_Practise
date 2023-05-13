"""
2nd way to store & get

Here we will get to know about
1) CLASS METHODS
2) INSTANCE METHODS
"""


class Employee:
    def store_emp_name(self, name):
        # All logic to store data in db/file etc will come here
        self.name = name

    def get_emp_name(self):
        # All logic to get data in db/file etc will come here
        return self.name

    @classmethod
    def store_company_name(cls, company_name):
        # All logic to store data in db/file etc will come here
        cls.company_name = company_name

    @classmethod
    def get_company_name(cls):
        # All logic to get data in db/file etc will come here
        return cls.company_name


# Create 2 objects
e1 = Employee()
e2 = Employee()


# -----------------
# Store the values in all 3 objects
# -----------------
# Employee.store_company_name(Employee, "XYZ Company") # Not required to pass 'Employee'
Employee.store_company_name("XYZ Company")
# automatically object 'Employee' will go as 1st argument

# e1.store_emp_name("e1", "emp-1") # Not required to pass "e1"
e1.store_emp_name("emp-1") # automatically "e1" will go as 1st argumrnt

# e2.store_emp_name("e2", "emp-2") # Not required to pass "e2"
e2.store_emp_name("emp-2") # automatically "e2" will go as 1st argumrnt
# cls : to hold class object reference
# self : to hold instance object reference
# -----------------

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
