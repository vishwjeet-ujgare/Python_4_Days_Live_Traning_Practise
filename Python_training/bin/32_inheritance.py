"""
Inheritance

Requirement: Add below functionality to existing class salary using
inheritance
Requirement-1: add_tax
Requirement-2: view_tax
Requirement-3: alter view_salary method to return "salary-tax"
"""

class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def view_salary(self):
        return self.salary

class Employee(Salary):
    # Requirement-1: add_tax
    def add_tax(self, tax):
        self.tax = tax

    # Requirement - 2: view_tax
    def view_tax(self):
        return self.tax


    # Requirement-3: alter view_salary method to return "salary-tax"
    # POLYMORPHISM: We can reuse same name as super class
    def view_salary(self): # This will OVERRIDE
        return self.salary - self.tax


e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.view_salary())
print("Tax:", e1.view_tax())


##########################
# Add functionality to existing class 'list'
##########################
class my_new_list(list):
    def add_my_name(self, my_name):
        self.my_name = my_name
    def view_my_name(self):
        return self.my_name

L1 = my_new_list([100,200, 300])
print("L1:", L1)
L1.append(400)
print("L1 after append 400:", L1)
L1.add_my_name("abc")
print("view my_name: ", L1.view_my_name())
##########################

##########################
# Multiple Inheritance
##########################
class A:
    pass

class B:
    pass

# Class C is inheriting from multiple classes A & B
class C(A, B):
    pass

##########################