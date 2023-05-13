"""
4. Tuple: We have predefined/builtin option to store collection of values like tuple of names, tuple of email-ids, tuple of addresses etc
            - But as of now we dont know how to store
            - IMMUTABLE: After creating tuple of values, throught the program we can't after/modify
                (we CAN'T add / we CAN'T delete / We CAN'T update)
            - Automatically index number will be assigned to each value
"""


print("tuple PART-1")
print("How to store the values and print")
print("-"*20)
# --------------------

my_tuple_1 = (10, 12.5, "Python", [100, 200])
# internally it will create object of predefined/builtin class 'tuple' and store the values

# OR

my_tuple_2 = tuple() # EMPTY OBJECT/tuple

my_tuple_3 = tuple([10, 12.5, "Python", [100, 200]])

print(my_tuple_1, my_tuple_2, my_tuple_3, sep="\n")

print("#"*40, end="\n\n")
####################################

print("tuple PART-2")
print("Indexing is similar to strings")
print("-"*20)
# --------------------

my_tuple = (10, 12.5, "Python", [100, 200])
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # "Python"
print("2nd character in Course Name:", my_tuple[2][1], end="\n\n") # "y"

print("Inner tuple:", my_tuple[3]) # [100, 200]
print("1st value in Inner tuple:", my_tuple[3][0]) # 100

print("#"*40, end="\n\n")
####################################


print("tuple PART-3")
print("Methods inside 'tuple' class")
print("-"*20)
# --------------------

print(dir(tuple), end="\n\n")

# OR
print(dir(my_tuple))

print("#"*40, end="\n\n")
####################################

print("tuple PART-4")
print(" 'count' method")
print("-"*20)
# --------------------

my_tuple = (10, 12.5, "Python", [100, 200])
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("Python")
print("count_of_python:", count_of_python)

print("#"*40, end="\n\n")
####################################

my_tuple[3].append(300)
print("my_tuple after append:", my_tuple)
