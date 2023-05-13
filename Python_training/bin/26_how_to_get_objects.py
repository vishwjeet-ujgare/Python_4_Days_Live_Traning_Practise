"""
How to get objects?
- Using classes we can create 1 or more objects

In this section, we will get to know about,
1) CLASS OBJECT
2) INSTANCE OBJECT
"""


class Employee:
    pass
# Use pass keyword to keep empty block
# Eventhough it is empty class, it will valid class only


# Create 2 objects
e1 = Employee()
e2 = Employee()

# Total 3 objects we have
# CLASS OBJECT: 'Employee', by default with the class name also one object is created
# INSTANCE OBJECTS: e1 & e2 are called INSTANCE objects which we create

print("Brand New Empty CLASS OBJECT 'Employee':", Employee)
print("Brand New Empty INSTANCE OBJECT 'e1':", e1)
print("Brand New Empty INSTANCE OBJECT 'e2':", e2)


