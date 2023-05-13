"""
How to communicate(Read/Write) with external files(Text files)
Text files like .txt, .csv, .log, .mylog, .yourlog etc
Finally file which can be opened in NOTEPAD
"""

'''
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
'''

'''
We have functions for each step
Step-1: Connect to file
    - open function
Step-2: Read/Write
    - To Write: 1)write 2) writelines 3) print function
    - To Read: 1) read 2) readline 3) readlines 4) list/tuple/set/dictionary classes to read file
Step-3: Disconnect
    - flush() # Send data from buffer to file. It will NOT CLOSE the connection
    - close() # close will 1st call flush() then disconnect or close the connection 
'''
print("All write operations")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
# my_file_handle = open("provide file name or file path here", "provide mode here")
my_file_handle = open("my_out_file.txt", "w")
# mode "w": It will create new file
# mode "w": It will ERASE the complete data if present in the file
# mode "w": Write only

# Step-2: Write
# --------------------

# Our data
x = 10
s = "Python\n"

# Convert other type of data into string becasue 1)write & 2) writelines
#   methods expects data in strings
x = str(x) + "\n"

# 1) write : Use this option when we have data in single string which
#   we want to write to file. Means, write will take single string of any length
my_file_handle.write(x) # It will Send data to buffer
my_file_handle.write(s) # It will Send data to buffer
my_file_handle.flush() # It will send data present in buffer to file (my_out_file.txt)

# 2) writelines: Use this option when we have data in any collection
#   like list/tuple etc. Means, writelines will take collection of values
my_data_in_list = [x, s]
my_file_handle.writelines(my_data_in_list)
my_file_handle.flush()

# 3) print function
# not required to add \n
x = x.strip() # remove\n or extra spaces
s = s.strip() # remove\n or extra spaces
print(x, s, 20, "Java", sep="\n", end="", file=my_file_handle, flush=True)
# 20-> not required to convert to string

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("""
All write operations completed.
Please check my_out_file.txt
""")

print("#"*40, end="\n\n")
####################################


print("Read operations: 1) read")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
file_content = my_file_handle.read()
# read(): will return COMPLETE file content in single string
print("file_content:", file_content)
print("file_content in RAW FORMAT:", repr(file_content))

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("#"*40, end="\n\n")
####################################


print("Read operations: 2) readline")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
file_content = my_file_handle.readline()
print("1st line:", file_content)

file_content = my_file_handle.readline()
print("2nd line:", file_content)

file_content = my_file_handle.readline()
print("3rd line:", file_content)

# Internally it uses pointer called 'seek' to track the lines
# seek(charater_index, line_no)

# Set seek to 0th position. ie beginning of the file
my_file_handle.seek(0)
file_content = my_file_handle.readline()
print("1st line:", file_content)

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("#"*40, end="\n\n")
####################################

print("Read operations: 3) readline by line using for-loop")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# --------------------
my_file_handle.close()

print("#"*40, end="\n\n")
####################################


print("Read operations: 4) readlines, list, tuple, set, dict")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create file if not present. FileNotFoundError

# Step-2: Read
# --------------------
file_content = my_file_handle.readlines()
# return complete data in list
print("File_content using readlines():", file_content, end="\n\n")
# Seek reached EOF

# set seek to beginning of the file
my_file_handle.seek(0)
file_content = list(my_file_handle)
print("file_content in list:", file_content, end="\n\n")
# Seek reached EOF


# set seek to beginning of the file
my_file_handle.seek(0)
file_content = tuple(my_file_handle)
print("file_content in tuple:", file_content, end="\n\n")
# Seek reached EOF

# set seek to beginning of the file
my_file_handle.seek(0)
file_content = set(my_file_handle)
print("file_content in set:", file_content, end="\n\n")
# Seek reached EOF

# set seek to beginning of the file
my_file_handle.seek(0)
file_content = dict(enumerate(my_file_handle))
print("file_content in dict:", file_content, end="\n\n")
# Seek reached EOF

# Step-3: Disconnect
# --------------------
my_file_handle.close()

# COMMENT:
# Example-1
# >>> L = [10, 20, 30]
# >>> dict(L)
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     dict(L)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
#
# Example-2:
# >>> M = [(0,10), (1,20), (2,30)]
# >>> dict(M)
# {0: 10, 1: 20, 2: 30}
#
# Example-3:
# >>> L
# [10, 20, 30]
# >>> e = enumerate(L)
# >>> list(e)
# [(0, 10), (1, 20), (2, 30)]
# >>>

print("#"*40, end="\n\n")
####################################

# --------------------
# Modes
# --------------------
# mode "w": Write Only, It will create new file, It will ERASES exisitng file content
# mode "r": Read Only, It will not create file if file not present
# mode "a": Append Only, It will create new file only if file not present
# mode "w+": RW, It will create new file, It will ERASES exisitng file content
# mode "r+": RW, It will not create file if file not present
# mode "a+": RW, It will create new file only if file not present
#           my_file_handle.write/.read
# --------------------
