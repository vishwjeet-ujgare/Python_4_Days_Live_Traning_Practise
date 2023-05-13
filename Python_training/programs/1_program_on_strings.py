"""
From the below string,
extract
IP
PICS

-----------------
Expected Output:
-----------------
123.123.123.123
wpaper.gif
-----------------
"""

print("How input data looks like?")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(in_string)

print("#"*40, end="\n\n")
####################################

print("How input data looks like in RAW FORMAT?")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(repr(in_string))

print("#"*40, end="\n\n")
####################################

print("What type of data we are receiving?")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(in_string))

print("#"*40, end="\n\n")
####################################

print("Methods inside the str class which we can make use to get output")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(dir(in_string))

print("#"*40, end="\n\n")
####################################

print("Extract IP - 1 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = in_string[0:15]
print(ip)

print("#"*40, end="\n\n")
####################################

print("Extract IP - 2 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

# 1-way
# in_string.index('3') # WONT WORK

# 2-way
# in_string.index(" ") # IT WILL WORK

# 3- way : If many spaces found in the beginnin
# in_string.index(" - - [") # It will also return index of 1st char of substring i.e SPACE

index_of_1st_space = in_string.index(" ")
ip = in_string[0:index_of_1st_space]
print(ip)

print("#"*40, end="\n\n")
####################################


print("Extract IP - 3 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = in_string.split()
print(sp)
ip = sp[0]
print(ip)

print("#"*40, end="\n\n")
####################################

print("Extract PICS - 1 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_pics = in_string.index("/pics/")
start_index = index_of_pics + 6

# 1-way
# end_index = in_string.index("HTTP")
# end_index = end_index - 1

# 2-way
end_index = in_string.index(" ", start_index)

img = in_string[start_index:end_index]
print(img)

print("#"*40, end="\n\n")
####################################

print("Extract PICS - 2 -way")
print("-"*20)
# --------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = in_string.split()
print(sp)

raw_img = sp[6] # '/pics/wpaper.gif'

# Remove /pics/ 1-way
img_1 = raw_img[6:]

# Remove /pics/ 2-way
img_2 = raw_img.removeprefix("/pics/")

print(img_1, img_2, sep="\n")

print("#"*40, end="\n\n")
####################################
