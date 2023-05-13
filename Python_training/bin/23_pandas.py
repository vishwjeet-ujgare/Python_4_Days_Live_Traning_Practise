"""
About Pandas
- pandas is one library
- having many classes & functions in it
- one of the class name is 'DataFrame'
- inside 'DataFrame' class we have methods related to
    tabular-data/2d-data/rows-columns-data/csv-data/xslx-data
"""

import pandas as pd

print("my_df_1")
print("How to store the values and print")
print("-"*20)
# --------------------

# Only 2d data w can store
my_df_1 = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
print(my_df_1)

print("#"*40, end="\n\n")
####################################


print("my_df_2")
print("How to store the values and print")
print("-"*20)
# --------------------

# Only 2d data w can store
my_df_2 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], columns=["c1", "c2", "c3"], index=["r1", "r2"])
print(my_df_2)

print("#"*40, end="\n\n")
####################################

print("methods inside 'DataFrame' class")
print("-"*20)
# --------------------

print(dir(my_df_1))

print("#"*40, end="\n\n")
####################################
