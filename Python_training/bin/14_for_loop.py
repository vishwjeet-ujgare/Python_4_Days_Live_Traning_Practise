"""
for loop: We are using to iterate any collection like str,list, tuple etc
"""

print("Without using for-loop, print each char in string")
print("-"*20)
# --------------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

print("Each Char:", my_string[0])
print("Each Char:", my_string[1])
print("Each Char:", my_string[2])
print("Each Char:", my_string[3])
print("Each Char:", my_string[4])
print("Each Char:", my_string[5])

print("#"*40, end="\n\n")
####################################


print("Using for-loop, print each char in string")
print("-"*20)
# --------------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

# for "provide_some_variable_name_here" in "provide_any_collection_here"

# Requirement is to print each character
for each_char in my_string:
    print("Each Char:", each_char)

print("#"*40, end="\n\n")
####################################

print("for loop-with list/tuple/set/Any other collections")
print("-"*20)
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")

for each_value in my_courses:
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
####################################

print("for-with dictionary.keys()")
print("-"*20)
# --------------------

my_dictionary = {"course": "python", "duration": 4, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
for each_key in my_dictionary.keys():
    print("Key:", each_key)
    print("Value for that key:",my_dictionary[each_key],end="\n\n" )


print("#"*40, end="\n\n")
####################################

print("for-with dictionary.values()")
print("-"*20)
# --------------------

my_dictionary = {"course": "python", "duration": 4, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.values()
# dict_values(['python', 4, 'online'])

for each_value in my_dictionary.values():
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
####################################

print("for-with dictionary.items()")
print("-"*20)
# --------------------

my_dictionary = {"course": "python", "duration": 4, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.items()
# dict_items([('course', 'python'), ('duration', 4), ('mode', 'online')])
for each_item in my_dictionary.items():
    print("Item:", each_item)
    print("Key:", each_item[0])
    print("Value:", each_item[1], end="\n\n")

print("#"*40, end="\n\n")
####################################

print("for-with dictionary.items()-2 way")
print("-"*20)
# --------------------

my_dictionary = {"course": "python", "duration": 4, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.items()
# dict_items([('course', 'python'), ('duration', 4), ('mode', 'online')])
for each_key, each_value in my_dictionary.items():
    print("Key:", each_key)
    print("Value:", each_value, end="\n\n")

print("#"*40, end="\n\n")
####################################

# 2 Cases:
# Case-1: How to end for loop in between
# CAse-2: How to skip current iteration & go for next iteration

print("# Case-1: How to end for loop in between")
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")


# Requirement: Check are there any course starting with 'Java'
#   if one course found then no need to check for other course


for each_course in my_courses:
    if each_course.startswith("Java"):
        print("Found")
        break

print("#"*40, end="\n\n")
####################################

print("# Case-2: How to skip current iteration & go for next iteration")
print("-"*20)
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")

for each_course in my_courses:
    if not each_course.startswith("Java"):
        continue
    # Below code applicable for Java Courses
    print("This Java Course Name is:", each_course)
    print("This is one version of java")
    print("This java course duration is 4 days", end="\n\n")

print("#"*40, end="\n\n")
####################################
