"""
Operator Overloading: We can support for any oprtators like +, - etc
in our class as well

Example :
- int class use + to add 2 nos
- str class use + to concatinate 2 strings

In python, we have special name given to each operator
like
+ = __add__
- = __sub__
If we want to support in our class then we need to write method for
each operator using special name

"""

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other): # self=e1, other=e2
        # return 0
        result = self.name + " : " + other.name
        return result

e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # e1.__add__(e2) # __add__(e1,e2)
print("result:", result)
