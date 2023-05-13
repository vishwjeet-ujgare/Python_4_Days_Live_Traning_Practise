"""
Get website data and print
"""

print("Get website data and print")
print("-"*20)
# --------------------

import urllib.request as ur

# Step-1: Connect
# --------------------
my_web_file_handle = ur.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

# Step-2: Read
# --------------------
web_content = my_web_file_handle.read()

# Step-3: Disconnect
# --------------------
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
####################################

print("type of web_content")
print("-"*20)
# --------------------

print(type(web_content))

print("#"*40, end="\n\n")
####################################

print("Methods inside 'bytes' class")
print("-"*20)
# --------------------

print(dir(web_content))

print("#"*40, end="\n\n")
####################################

print("convert bytes to string")
print("-"*20)
# --------------------

web_content = web_content.decode()
print(type(web_content))

print("#"*40, end="\n\n")
####################################

print("web_content")
print("-"*20)
# --------------------

print(web_content)

print("#"*40, end="\n\n")
####################################
