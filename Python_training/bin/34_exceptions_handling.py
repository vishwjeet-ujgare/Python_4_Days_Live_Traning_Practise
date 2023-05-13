"""
Exceptions handling
"""

# print("Without handling exceptions")
# print("-"*20)
# # --------------------
#
# a = 10
# b = 0
# c = a/b # Program will terminate here abruptly
# print("c:",c)
#
# print("#"*40, end="\n\n")
# ####################################

print("try-except")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    c = a/b # Program will not termintate here, instead control will be passed to 'except' block
    print("c:",c)
except:
    print("Some error in try block =, so reached except block")
    print("Write logic to solve error occurred in try")
    # import sys
    # sys.exit(0) # If we want to terminte the program

print("#"*40, end="\n\n")
####################################

# --------------------
# Observations
# --------------------
# - In above example,we will not able to decide what type of
#   error occured in 'try' block
# --------------------

# --------------------
# - For each exception we need to have classes
# - few exception classes are present in builtins
# - All exception classes are inherited from 'Exception'
# - We can mention class name in 'except'
# --------------------

print("try-except with class names")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    c = a/x # Name Error
    print("c:",c)
except ZeroDivisionError: # 1st way to mention class name
    print("It is ZDE")
except NameError as ne: # 2nd way to mention class name, where we are capturing thrown object
    print("It is NE and ne is:", ne)
except (KeyError, IndexError):
    print("it can be either KE or IE")

print("#"*40, end="\n\n")
####################################

print("try-except-else")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    c = a/b
    print("c:",c)
    # Example: DB connection logic here
except:
    # Handle only DB connection Error Here
    print("Some error in try block, so reached except block")
else:
    # If DB connection success then execute queries here
    print("Executing Else Block")

# if "try" success then execute "else" block and skip "except" block
# if "try" failed then execute "except" block and skip "else" block

print("#"*40, end="\n\n")
####################################

print("try-except-else-finally")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    c = a/b
    print("c:",c)
    # Example: DB connection logic here
except:
    # Handle only DB connection Error Here
    print("Some error in try block, so reached except block")
else:
    # If DB connection success then execute queries here
    print("Executing Else Block")
finally:
    print("Executing Finally Block")
    # Example:Close DB connection here
    # any cleanup activity we can use this


# if "try" success/failed but finally will execute
# if "except" success/failed but finally will execute
# if "else" success/failed but finally will execute
# So, finally will always execute

print("#"*40, end="\n\n")
####################################

print("assert")
print("-"*20)
# --------------------

try:
    a = 10
    b = 0
    assert b > 0
    # If condition fails then throw AssertionError
    c = a/b
    print("c:",c)
except AssertionError:
    print("This AError")


print("#"*40, end="\n\n")
####################################

print("raise")
print("-"*20)
# --------------------

# 'assert' will always throw assertion error
# in 'raise', we can specify type of error to throw

try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError
    c = a/b
    print("c:",c)
except ZeroDivisionError:
    print("This AError")


print("#"*40, end="\n\n")
####################################

print("Custom Exception Class-1")
print("-"*20)
# --------------------

# Minimum requirement to create exception class is,
# it should be sub class of 'Exception' class
# OR if some class is already subclass of 'Excpeiont' then we can also
# create sub class of that class like ZeroDivisionError, NameError etc

class MyError(Exception):
    pass # Eventhough it empty, it is valid exception class

try:
    a = 10
    b = 0
    if b == 0:
        raise MyError
    c = a/b
    print("c:",c)
except MyError:
    print("This MyError")


print("#"*40, end="\n\n")
####################################

print("Custom Exception Class-2")
print("-"*20)
# --------------------

# Requirement: Pass some message while raising the exception

class MyError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

try:
    a = 10
    b = 0
    if b == 0:
        raise MyError("Here b value is 0 so raising MyError")
    c = a/b
    print("c:",c)
except MyError as me:
    print("This MyError and details are:", me.error_message)


print("#"*40, end="\n\n")
####################################
