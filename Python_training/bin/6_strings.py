"""
2. Strings: We have predefined/builtin option to store collection of characters like name, email-id, address etc
            - But as of now we dont know how to store
            - IMMUTABLE
            - Automatically index number will be assigned to each character            
"""

print("Strings PART-1")
print("How to store and print")
print("-"*20)
# --------------------

a = 'PERSON'
# Internally it will create object of predefined/builtin class 'str' and store the values

#OR
b = str() # EMPTY str object
c = str('PERSON')
print(a, b, c, sep="\n")

print("#"*40, end="\n\n")
####################################

print("Strings PART-2")
print("How to store and print")
print("-"*20)
# --------------------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = '''PERSON'S HEIGHT IS XYZ" (" represents inches)'''
e = """PERSON'S HEIGHT IS XYZ" (" represents inches)"""

# If we are not assinging to any variable then it will be comment
# Below one is comment
"""PERSON'S HEIGHT IS XYZ" (" represents inches)"""

print(a, b, c, d, e, sep="\n")

print("#"*40, end="\n\n")
####################################


print("Strings PART-3")
print("How to store and print")
print("-"*20)
# --------------------

a = "C:\newfolder\test.py"
# By default, inside string, we are using \with some characters for special purpose
# examplE: \n-> replace with new line \t> replace with tab space

# if we want as \n\t as it is then
b = r"C:\newfolder\test.py"
# r-> raw string, dont replace \n\t etc

print("a:",a)
print("b:",b)
print("convert existind string 'a' to RAW FORMAT:", repr(a))

print("#"*40, end="\n\n")
####################################


print("Strings PART-4")
print("How to store and print")
print("-"*20)
# --------------------

x = 10
y = 20
z = x + y

result = f"add of {x} and {y} is {z}"
# f-> format: It replace {variable_name} with value

print("result:", result)

print("#"*40, end="\n\n")
####################################

print("Strings PART-5")
print("Indexes: Access each character using index")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-1
print("0th character using +ve index no:", my_string[0])
print("0th character using -ve index no:", my_string[-8], end="\n\n")

# print("100th character using +ve index no:", my_string[100]) # IndexERROR
print("#"*40, end="\n\n")
####################################

print("Strings PART-6")
print("SLICING: We can get substring")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-2
print("Substring from index 1 to 6 using + ve index no:", my_string[1:6])
print("Substring from index 1 to 6 using - ve index no:", my_string[-7:-2])
print("Substring from index 1 to 6 using + ve/-ve index no:", my_string[1:-2])
print("Substring from index 1 to 6 using + ve/-ve index no:", my_string[-7:6], end="\n\n")

print("Substring from index 1 to END using + ve index no:", my_string[1:])
print("Substring from index 1 to END using - ve index no:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to 6 using + ve index no:", my_string[:6])
print("Substring from BEGINNING to 6 using - ve index no:", my_string[:-2])

print("Substring from BEGINNING to END :", my_string[:])

print("#"*40, end="\n\n")
####################################

print("Strings PART-7")
print("STEP VALUE: We can skip characters")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-3
print("Substring from index 1 to 6 using + ve index no default step by '1':", my_string[1:6])
print("Substring from index 1 to 6 using - ve index no default step by '1':", my_string[-7:-2], end="\n\n")
# By default Step Value=1
# Which means, from 1 to 6 give me every character

print("Substring from index 1 to 6 using + ve index no step by '1':", my_string[1:6:1])
print("Substring from index 1 to 6 using - ve index no step by '1':", my_string[-7:-2:1], end="\n\n")
# Step Value=1
# Which means, from 1 to 6 give me every character

print("Substring from index 1 to 6 using + ve index no step by '2':", my_string[1:6:2])
print("Substring from index 1 to 6 using - ve index no step by '2':", my_string[-7:-2:2], end="\n\n")
# Step Value=2
# Which means, from 1 to 6 give me every 2nd character
# by default, character at start index will always come, after that every 2nd character

print("#"*40, end="\n\n")
####################################

print("Strings PART-8")
print("What is there inside 'str' object")
print("-"*20)
# --------------------

#  1- way
print(dir(str), end="\n\n")
# OR
# 2-way
print(dir(my_string))

# __some_name__ are internally being used by some-operator/some-function
# Example:
# >>> "-"*20
##'--------------------'
##>>> "-".__mul__(20)
##'--------------------'
##>>> s="Hello"
##>>> len(s)
##5
##>>> s.__len__()
##5


print("#"*40, end="\n\n")
####################################

print("Strings PART-9")
print(" 'startswith' method")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.startswith("WEL") # True/False
print('my_string.startswith("WEL"):', result) # True

print("#"*40, end="\n\n")
####################################

print("Strings PART-10")
print(" 'split' method")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.split() # split by SPACE, and return splitted values in list
print("my_string.split():", result) # ["WEL", "COME"]

result = my_string.split("E") # 
print('my_string.split("E"):', result) # [ 'W' , 'L COM', '']

print("#"*40, end="\n\n")
####################################

print("Strings PART-11")
print(" 'removeprefix' method")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.removeprefix("WEL ")
print('my_string.removeprefix("WEL "):', result)

print("#"*40, end="\n\n")
####################################

print("Strings PART-12")
print(" 'index' method")
print("-"*20)
# --------------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.index('E') # return index of 1st occurance of E
print("my_string.index('E'):", result)

result = my_string.index('E', 3) # return index of E BUT start looking from index 3 onwards
print("my_string.index('E'):", result)

print("#"*40, end="\n\n")
####################################
