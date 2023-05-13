"""
Functions with POSITIONAL ARGUMENTS

Case-2: How to pass values to the varaibles present inside the function
        (how to pass values to name, company)

2 ways pass values
1st way is: We can pass only values to name, comapny
2nd way is: We can pass values to name, comapny using name=value, company=value format

Here, we will discuss
1st way is: We can pass only values to name, comapny
"""

print("Function with positional arguments")
print("-"*20)
# --------------------


# name, company are called positional arguments
def employee(name, company):
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return [name, company]


received_value = employee("emp-1", "XYZ Company")
print("received_value:", received_value)


received_value = employee("emp-2", "XYZ Company")
print("received_value:", received_value)


received_value = employee("emp-3", "ABC Company")
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with DEFAULT VALUE positional arguments")
print("-"*20)
# --------------------


# name, company are called positional arguments
def employee(name, company="XYZ Company"): # order, 1st list all non-defalut then default
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return [name, company]


received_value = employee("emp-1") # default value for company will be used
print("received_value:", received_value)


received_value = employee("emp-2", "XYZ Company")
print("received_value:", received_value)


received_value = employee("emp-3", "ABC Company")
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("Function with VARIABLE positional arguments")
print("-"*20)
# --------------------


# *prev_companies called VARIABLE positional arguments
def employee(name, company="XYZ Company", *prev_companies):
    print("Emp Name:", name)
    print("prev_companies:", prev_companies)
    print("Company:", company, end="\n\n")
    return [name, company, prev_companies]


received_value = employee("emp-1") # default value for company will be used
# prev_companies=()
print("received_value:", received_value)


received_value = employee("emp-2", "XYZ Company")
# prev_companies=()
print("received_value:", received_value)


received_value = employee("emp-3", "ABC Company", "prev_comp_1")
# prev_companies=("prev_comp_1")
print("received_value:", received_value)

received_value = employee("emp-3", "ABC Company", "prev_comp_1", "prev_comp_2")
# prev_companies=("prev_comp_1", "prev_comp_2")
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################
