"""
Here,
2nd way is: We can pass values to name, comapny using name=value, company=value format
"""


print("Function with keyword or named arguments")
print("-"*20)
# --------------------


# name, company are called keyword or named arguments
def employee(*, name, company):
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return [name, company]


received_value = employee(name="emp-1", company="XYZ Company")
print("received_value:", received_value)


received_value = employee(company="XYZ Company", name="emp-2" )
print("received_value:", received_value)


received_value = employee(name="emp-3", company="ABC Company")
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################


print("Function with DEFAULT VALUE keyword or named arguments")
print("-"*20)
# --------------------


# name, company are called keyword or named arguments
def employee(*, name, company="XYZ Company"):
    print("Emp Name:", name)
    print("Company:", company, end="\n\n")
    return [name, company]


received_value = employee(name="emp-1") # default value for company will be used
print("received_value:", received_value)


received_value = employee(name="emp-2", company="XYZ Company")
print("received_value:", received_value)


received_value = employee(name="emp-3", company="ABC Company")
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################


print("Function with VARIABLE keyword or named arguments")
print("-"*20)
# --------------------


# **prev_companies called VARIABLE keyword or named arguments
def employee(*, name, company="XYZ Company", **prev_companies):
    print("Emp Name:", name)
    print("prev_companies:", prev_companies)
    print("Company:", company, end="\n\n")
    return [name, company, prev_companies]


received_value = employee(name="emp-1") # default value for company will be used
# prev_companies={}
print("received_value:", received_value)


received_value = employee(name="emp-2", company="XYZ Company")
# prev_companies={}
print("received_value:", received_value)


received_value = employee(name="emp-3", company="ABC Company", pc1="prev_comp_1")
# prev_companies={pc1:"prev_comp_1"}
print("received_value:", received_value)

received_value = employee(name="emp-3", company="ABC Company", pc1="prev_comp_1", pc2="prev_comp_2")
# prev_companies={pc1:"prev_comp_1", pc2:"prev_comp_2"}
print("received_value:", received_value)

print("#"*40, end="\n\n")
####################################

print("All types of args in ONE function")
print("-"*20)
# --------------------


# We can combine both positional & named arguments in single function
def add(a, b=10, *c, d, e=20, **f):
    return a + b + sum(c) + d + e + sum(f.values())


add_result_1 = add(10, d=20)
# a = 10, b = 10, c = ()
# d = 20, e = 20, f = {}
print("add_result_1:", add_result_1) # 60

add_result_2 = add(10, 20, 30, 40, 50, d = 60, e=70, x=80, y=90, z=100)
# a = 10, b = 20, c = (30, 40, 50)
# d = 60, e = 70, f = {x:80, y:90,z:100}
print("add_result_2:", add_result_2) # 550

print("#"*40, end="\n\n")
####################################
