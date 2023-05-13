"""
What python library means?
and
Complete Python Programming Language Structure
"""

# ---------------
# What python library means?
# ---------------
# - python library can be one or more modules like mymodule.py
# - python library can be one or more packages like mypackage
# - python library can be one or more frameworks
#     - framework is like mymodule or mypackage only
#       but in case of mymodule or mypackage, we are keeping only definitions
#       but in case of framework some of the common logics are implemented
#     - Example: testing framework where test cases for each project is different
#       but executing all test cases, producing summary, reports etc are common.
#       these common things are implemented
# ---------------

# ---------------
# Complete Python Programming Language Structure
# ---------------
# PART-1: Python Programming Language
#        - data types, if, for, while, file operations, functions,
#           modules, packages, classes, exceptions handling, etc
#        - Using PARt-1, we can develop anything from scratch
#        - We already developed: program-1 to program-5
# ---------------
# PART-2: Builtins
#       - Few variables, functions & classes are predefined
#       - By default it is imported
#       - Which we can make use of it
#       - Complete builtins list: print(dir(__builtins__))
#       - We used: print, int, float, str, list, tuple, dict, set, frozenset,
#           dir, type, enumerate etc
# ---------------
# PART-3: Standard Libraries
#       - Few libraries are getting installed when we install python
#       - difference with builtins is,
#           builtins are by default imported
#           but
#           standard libraries we need to import and use
#       - Location: C:\Python311\Lib
#       - Documentation: https://docs.python.org/3/library/index.html
# ---------------
# PART-4: 3rd Party / External Libraries
#       - MAIN BIG repository for all python libraries
#       - Location: https://pypi.org/
#       - Documentation: https://pypi.org/
#       - This we need to download and install
# ---------------
# PART-5: Custom Libraries
#       - Which we develop
#       - We already developed,
#           1) mymodule.py
#           2) mypackage
# ---------------

# pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org flask
