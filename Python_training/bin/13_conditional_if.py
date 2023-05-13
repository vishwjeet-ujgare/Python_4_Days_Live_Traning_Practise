"""
conditional statement 'if': Based on the condition if we want to execute
block of statements

In some languages
if some_condition
{
    s1
        s2
    s3
}
s4

In python, we wont use {} to make block instead we use indentation
if some_condition
    s1
    s2
    s3
s4
"""
print("Only 'if'")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")

if x > 10:
    print("Value of x is greater than 10")

if x < 10:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
####################################

print("if-elif")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")

elif x > 10:
    print("Value of x is greater than 10")

elif x < 10:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
####################################

print("if-elif-else")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")

elif x > 10:
    print("Value of x is greater than 10")

else:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
####################################

print("if-with strings")
print("-"*20)
# --------------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

if my_string != "Java" and my_string != "C++":
    print("Not Java/C++")

if not my_string.startswith("Perl"):
    print("Not Perl")

if "tho" in my_string:
    print("Substring 'tho' found")

print("#"*40, end="\n\n")
####################################

print("if-with list/tuple/set/Any other collections")
print("-"*20)
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")

if "Java-1" in my_courses:
    print("Course 'Java-1' present")

print("#"*40, end="\n\n")
####################################

print("if-with dictionary")
print("-"*20)
# --------------------

my_dictionary = {"course": "python", "duration": 4, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
if "course" in my_dictionary.keys():
    print("Key 'course' Found")

# my_dictionary.values()
# dict_values(['python', 4, 'online'])
if "python" in my_dictionary.values():
    print("Value 'python' present")

# my_dictionary.items()
# dict_items([('course', 'python'), ('duration', 4), ('mode', 'online')])
if ('course', 'python') in my_dictionary.items():
    print("Item '('course', 'python')' Present")

print("#"*40, end="\n\n")
####################################

