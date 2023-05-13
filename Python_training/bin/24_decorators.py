"""
Decorators: IF we are writing more than one function where
in each function few-logic/few-statements are common
then how to reuse?

- Answer is we need to write function for reusing the code

How to write common function to reuse it??
"""

print("Without using decorators")
print("-"*20)
# --------------------


def add1(a,b):
    print("Result is")
    print(a+b)
    print("End of the result", end="\n\n")


def add2(a,b):
    print("Result is")
    print(a+b+b)
    print("End of the result", end="\n\n")


def sub1(a,b):
    print("Result is")
    print(a-b)
    print("End of the result", end="\n\n")


def sub2(a,b):
    print("Result is")
    print(a-b-b)
    print("End of the result", end="\n\n")


add1(10, 20)
add2(10, 20)
sub1(10, 20)
sub2(10, 20)

print("#"*40, end="\n\n")
####################################


print("my common function - 1: WRONG DESIGN")
print("-"*20)
# --------------------

def my_common_func():
    print("Result is")
    print("End of the result")

def add1(a,b):
    my_common_func()
    print(a+b)
    my_common_func()


def add2(a,b):
    my_common_func()
    print(a+b+b)
    my_common_func()


def sub1(a,b):
    my_common_func()
    print(a-b)
    my_common_func()


def sub2(a,b):
    my_common_func()
    print(a-b-b)
    my_common_func()


add1(10, 20)
add2(10, 20)
sub1(10, 20)
sub2(10, 20)

print("#"*40, end="\n\n")
####################################

print("Using Decorator Design Pattern - PARTIAL IMPLMENTATION")
print("-"*20)
# --------------------


def my_decorator(my_func):
    def decorated_func(x,y):
        print("Result is")
        my_func(x,y) # add1(10,20)
        print("End of the result", end="\n\n")
    return decorated_func


def add1(a,b):
    print(a+b)

inner_func = my_decorator(add1) # my_func=add1
# inner_func = decorated_func
inner_func(10,20) # x=10, y=20

def add2(a,b):
    print(a+b+b)

inner_func = my_decorator(add2) # my_func=add2
# inner_func = decorated_func
inner_func(10,20) # x=10, y=20


def sub1(a,b):
    print(a-b)

inner_func = my_decorator(sub1) # my_func=sub1
# inner_func = decorated_func
inner_func(10,20) # x=10, y=20

def sub2(a,b):
    print(a-b-b)

inner_func = my_decorator(sub2) # my_func=sub2
# inner_func = decorated_func
inner_func(10,20) # x=10, y=20


print("#"*40, end="\n\n")
####################################

print("Using Decorator Design Pattern - FINAL DECORATOR")
print("-"*20)
# --------------------


def my_decorator(my_func):
    def decorated_func(x,y):
        print("Result is")
        my_func(x,y) # add1(10,20)
        print("End of the result", end="\n\n")
    return decorated_func

@my_decorator
def add1(a,b):
    print(a+b)

add1(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(add1) # my_func=add1
# inner_func(10,20) # x=10, y=20
# -------------

@my_decorator
def add2(a,b):
    print(a+b+b)

add2(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(add2) # my_func=add2
# inner_func(10,20) # x=10, y=20
# -------------

@my_decorator
def sub1(a,b):
    print(a-b)

sub1(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(sub1) # my_func=sub1
# inner_func(10,20) # x=10, y=20
# -------------
@my_decorator
def sub2(a,b):
    print(a-b-b)

sub2(10,20)

# -------------
# Not required now, @my_docorator will take care
# -------------
# inner_func = my_decorator(sub2) # my_func=sub2
# inner_func(10,20) # x=10, y=20
# -------------


print("#"*40, end="\n\n")
####################################
