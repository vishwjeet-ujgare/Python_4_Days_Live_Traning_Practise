"""
3. List: We have predefined/builtin option to store collection of values like list of names, list of email-ids, list of addresses etc
            - But as of now we dont know how to store
            - MUTABLE: After creating list of values, throught the program we CAN after/modify
                (we CAN add / we CAN delete / We CAN update)
            - Automatically index number will be assigned to each value
"""

print("List PART-1")
print("How to store the values and print")
print("-"*20)
# --------------------

my_list_1 = [10, 12.5, "Python", [100, 200]]
# internally it will create object of predefined/builtin class 'list' and store the values

# OR

my_list_2 = list() # EMPTY OBJECT/List

my_list_3 = list([10, 12.5, "Python", [100, 200]])

print(my_list_1, my_list_2, my_list_3, sep="\n")

print("#"*40, end="\n\n")
####################################

print("List PART-2")
print("Indexing is similar to strings")
print("-"*20)
# --------------------

my_list = [10, 12.5, "Python", [100, 200]]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # "Python"
print("2nd character in Course Name:", my_list[2][1], end="\n\n") # "y"

print("Inner list:", my_list[3]) # [100, 200]
print("1st value in Inner list:", my_list[3][0]) # 100

print("#"*40, end="\n\n")
####################################


print("List PART-3")
print("Methods inside 'list' class")
print("-"*20)
# --------------------

print(dir(list), end="\n\n")

# OR
print(dir(my_list))

print("#"*40, end="\n\n")
####################################

print("List PART-4")
print(" 'append' method")
print("-"*20)
# --------------------

my_list = [10, 12.5, "Python", [100, 200]]
print("my_list:", my_list, end="\n\n")

my_list.append("Java")
my_list[3].append(300)

print("my_list after append:", my_list)

print("#"*40, end="\n\n")
####################################

