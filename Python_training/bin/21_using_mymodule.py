"""
In this program, we are using variables, functions & classes
defined in mymodule.py
"""

print("about 'import'")
print("-"*20)
# --------------------
import mymodule
# - import will create one EMPTY object called 'mymodule'
# - import will execute mymodule.py
# - when we execute mymodule.py, 2 objects are getting created
#   1) location 2) log_process_func_kw_arg
# - import will keep both objects inside EMPTY object 'mymodule'
# - From mymodule object we can access it

print(dir(mymodule))

print("#"*40, end="\n\n")
####################################

print("1 - way to 'import'")
print("-"*20)
# --------------------

import mymodule
print("location:", mymodule.location)
print("log result:", mymodule.log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("2 - way to 'import'")
print("-"*20)
# --------------------

import mymodule as mm
print("location:", mm.location)
print("log result:", mm.log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################


print("3 - way to 'import'")
print("-"*20)
# --------------------

from mymodule import location, log_process_func_kw_arg
print("location:", location)
print("log result:", log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################


print("4 - way to 'import'")
print("-"*20)
# --------------------

from mymodule import location as lc, log_process_func_kw_arg as lpf
print("location:", lc)
print("log result:", lpf(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################


print("5 - way to 'import'")
print("-"*20)
# --------------------

from mymodule import *
print("location:", location)
print("log result:", log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################


# --------------------
# PACKAGES
# --------------------
# - if we create more and more modules then we can keep/store/organize
#   in folders & sub folders - these folders are called PACKAGES
# - we can directly import from packages
# --------------------

print("1 - way to 'import'")
print("-"*20)
# --------------------

import mypackage.aws.mymodule
print("location:", mypackage.aws.mymodule.location)
print("log result:", mypackage.aws.mymodule.log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("2 - way to 'import'")
print("-"*20)
# --------------------

import mypackage.aws.mymodule as mm
print("location:", mm.location)
print("log result:", mm.log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("3 - way to 'import'")
print("-"*20)
# --------------------

from mypackage.aws.mymodule import location, log_process_func_kw_arg
print("location:", location)
print("log result:", log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("4 - way to 'import'")
print("-"*20)
# --------------------

from mypackage.aws.mymodule import location as lc, log_process_func_kw_arg as lpf
print("location:", lc)
print("log result:", lpf(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################

print("5 - way to 'import'")
print("-"*20)
# --------------------

from mypackage.aws.mymodule import *
print("location:", location)
print("log result:", log_process_func_kw_arg(log_file_path="../log/server_log.txt"))

print("#"*40, end="\n\n")
####################################
