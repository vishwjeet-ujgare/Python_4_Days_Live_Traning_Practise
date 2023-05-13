"""
while loop: Based on the condition we can execute the loop
"""

print("While Example-1")
print("-"*20)
# --------------------

x = 0
while x < 10:
    print("Value of x is :", x)
    x = x + 1 # x += 1


print("#"*40, end="\n\n")
####################################

print("Using while-loop, print each char in string")
print("-"*20)
# --------------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

index_no = 0
while index_no < len(my_string):
    print("Each Char:", my_string[index_no])
    index_no = index_no + 1

# Requirement is to print each character
for each_char in my_string:
    print("Each Char:", each_char)

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

index_no = 0
while index_no < len(my_courses):
    if my_courses[index_no].startswith("Java"):
        print("Found")
        break
    index_no = index_no + 1
#
# for each_course in my_courses:
#     if each_course.startswith("Java"):
#         print("Found")
#         break

print("#"*40, end="\n\n")
####################################

print("# Case-2: How to skip current iteration & go for next iteration")
print("-"*20)
# --------------------

my_courses = ["Perl", "Java-1", "python", "Java-2", "C++"]
print("my_courses:", my_courses, end="\n\n")

index_no = 0
while index_no < len(my_courses):
    if not my_courses[index_no].startswith("Java"):
        index_no = index_no + 1
        continue
    # Below code applicable for Java Courses
    print("This Java Course Name is:", my_courses[index_no])
    print("This is one version of java")
    print("This java course duration is 4 days", end="\n\n")
    index_no = index_no + 1


# for each_course in my_courses:
#     if not each_course.startswith("Java"):
#         continue
#     # Below code applicable for Java Courses
#     print("This Java Course Name is:", each_course)
#     print("This is one version of java")
#     print("This java course duration is 4 days", end="\n\n")

print("#"*40, end="\n\n")
####################################
