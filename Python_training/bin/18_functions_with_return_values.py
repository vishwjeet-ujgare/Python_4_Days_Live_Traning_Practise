"""
2 Cases
Case-1: How to access values outside the function
        (how to acccess name, company values outside the function)
Case-2: How to pass values to the varaibles present inside the function
        (how to pass values to name, company)

Here,
we will discuss,
Case-1: How to access values outside the function
        (how to acccess name, company values outside the function)
"""

print("Function with 1 return value")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return name # provide which value we want to return


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with more than 1 return value: TUPLE")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return name, company # It will put all values in tuple & return


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################


print("Function with more than 1 return value: LIST")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return [name, company]


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################


print("Function with more than 1 return value: DICTIONARY")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return {"name": name, "company": company}


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with no return value: None")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with no return statement: None")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with one line expression in return ")
print("-"*20)
# --------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return (10+30)/(1+2) # return the result


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################
