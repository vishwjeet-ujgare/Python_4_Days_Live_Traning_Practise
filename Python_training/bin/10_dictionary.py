"""
5. Dictionary: We have predefined/builtin option to store collection of values like list of names, list of email-ids, list of addresses etc
            - But as of now we dont know how to store
            - MUTABLE: After creating list of values, throught the program we CAN after/modify
                (we CAN add / we CAN delete / We CAN update)
            - Automatically index number will NOT be assigned to each value,
            We can provide index number to each value: KEY/VALUE pair
"""

print("Dictionary PART-1")
print("How to store the values and print")
print("-"*20)
# --------------------

my_dictionary_1 = {0:"Python", 1:4, 2:"Online"}
# Internally it will create object of predefined/builtin class 'dict' and store the values

# OR
my_dictionary_2 = dict({0:"Python", 1:4, 2:"Online"})

# We can use any IMMUTABLE VALUEs for KEY like numbers, string, tuple etc
# Values can be anything
my_dictionary_3 = {"course":"Python", "duration":4, "mode":"Online"}

my_dictionary_4 = {
    "duration": 4,
    "course": "Python",
    "mode": ["online", "offline"],
    "author": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1: ", my_dictionary_1, end="\n\n")
print("my_dictionary_2: ", my_dictionary_2, end="\n\n")
print("my_dictionary_3: ", my_dictionary_3, end="\n\n")
print("my_dictionary_4: ", my_dictionary_4, end="\n\n")

print("#"*40, end="\n\n")
####################################

print("Dictionary PART-2")
print("Access each value by key")
print("-"*20)
# --------------------

my_dictionary = {
    "duration": 4,
    "course": "Python",
    "mode": ["online", "offline"],
    "author": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary: ", my_dictionary, end="\n\n")

print("Duration: ", my_dictionary["duration"], end="\n\n")

print("Course Name: ", my_dictionary["course"]) # "Python"
print("2nd character in Course Name: ", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("1st Mode:", my_dictionary["mode"][0]) # "online"
print("2nd character in 1st Mode:", my_dictionary["mode"][0][1], end="\n\n") # "n"

print("Author:", my_dictionary["author"]) # {"fname": "abc", "lname": "xyz"}
print("Author fname:", my_dictionary["author"]["fname"]) # "abc"
print("2nd character in Author fname:", my_dictionary["author"]["fname"][1], end="\n\n") # "b"

print("#"*40, end="\n\n")
####################################

print("Dictionary PART-3")
print("Methods inside 'dict' class")
print("-"*20)
# --------------------

print(dir(dict), end="\n\n")

# OR

print(dir(my_dictionary))

print("#"*40, end="\n\n")
####################################

print("Dictionary PART-4")
print("'values' method")
print("-"*20)
# --------------------

print(my_dictionary.values())

print("#"*40, end="\n\n")
####################################
