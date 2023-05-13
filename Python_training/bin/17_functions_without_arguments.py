"""
Functions: If we want to rewrite/copy-paste same code more than one time
then instead of rewrite/copy-paste, keep that code in one block and
execute that block 0 or more times

Coding style Guide:
# https://peps.python.org/pep-0008/

"""

print("Without using function")
print("-"*20)
# --------------------

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

print("#"*40, end="\n\n")
####################################

print("Using function")
print("-"*20)
# --------------------


# Function Definition
def my_func():
    a = 10
    b = 20
    c = a + b
    print("c:", c)


# Function Call
my_func()
my_func()
my_func()
my_func()
my_func()

print("#"*40, end="\n\n")
####################################

print("Just Another function: Nothing special Here")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")

employee()
employee()
employee()

print("#"*40, end="\n\n")
####################################
