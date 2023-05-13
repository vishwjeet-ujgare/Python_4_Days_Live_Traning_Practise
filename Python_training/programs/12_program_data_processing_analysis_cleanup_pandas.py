"""
Using Pandas
- Data analysis
- Data Cleanup
- Data processing
etc
"""

print("CSV to DF")
print("-"*20)
# --------------------

import pandas as pd

csv_data_df = pd.read_csv("db_dump_4.csv")

print(csv_data_df)

print("#"*40, end="\n\n")
####################################

print("type of csv_data_df")
print("-"*20)
# --------------------

print(type(csv_data_df))

print("#"*40, end="\n\n")
####################################

print("columns")
print("-"*20)
# --------------------

print(csv_data_df.columns)
# ['Unnamed: 0', 'IP', 'DATE', 'PICS', 'URL']

print("#"*40, end="\n\n")
####################################

print("Remove extra column 'Unnamed: 0'")
print("-"*20)
# --------------------

csv_data_df.drop('Unnamed: 0', axis=1, inplace=True)
# axis=1, remove vertically, 0 means horizontal
# inplace=True means, make changes in the same object 'csv_data_df'
print("After removing 'Unnamed: 0' columns ")
print(csv_data_df.columns)

print("#"*40, end="\n\n")
####################################

print("Create new column 'IP_PORT' with port no 8080 added IP column")
print("-"*20)
# --------------------

csv_data_df["IP_PORT"] = csv_data_df["IP"] + ":8080"

print(csv_data_df.head(3))

print("#"*40, end="\n\n")
####################################

print("columns order")
print("-"*20)
# --------------------

print(csv_data_df.columns)
# ['IP', 'DATE', 'PICS', 'URL', 'IP_PORT']

print("#"*40, end="\n\n")
####################################

print("columns after reorder")
print("-"*20)
# --------------------

# ['IP', 'IP_PORT', 'DATE', 'PICS', 'URL']
csv_data_df = csv_data_df[['IP', 'IP_PORT', 'DATE', 'PICS', 'URL']]
print(csv_data_df.columns)

print("#"*40, end="\n\n")
####################################

print("replace 'No Image' with 'abc.jpg'")
print("-"*20)
# --------------------

csv_data_df["PICS"].replace(["No Image"], "abc.jpg", inplace=True)
print(csv_data_df["PICS"])

print("#"*40, end="\n\n")
####################################

print("filter only jpg images records")
print("-"*20)
# --------------------

new_csv_data_df = csv_data_df[csv_data_df["PICS"].str.endswith("jpg")]
print(new_csv_data_df["PICS"])


print("#"*40, end="\n\n")
####################################

print("write cleaned data to file")
print("-"*20)
# --------------------

new_csv_data_df.to_csv("cleaned_data.csv", index=None)
print("Created 'cleaned_data.csv'")

print("#"*40, end="\n\n")
####################################

print("Total Count of PICS column")
print("-"*20)
# --------------------

print(csv_data_df["PICS"].count())

print("#"*40, end="\n\n")
####################################

print("Value Count of PICS column")
print("-"*20)
# --------------------

value_count_of_pics = csv_data_df["PICS"].value_counts()
print(value_count_of_pics)


print("#"*40, end="\n\n")
####################################

print("Value Count of PICS column")
print("-"*20)
# --------------------

value_count_of_pics = csv_data_df["PICS"].value_counts()
print(value_count_of_pics)


print("#"*40, end="\n\n")
####################################

print("Value Count of PICS column")
print("-"*20)
# --------------------

import matplotlib.pyplot as plt

value_count_of_pics = csv_data_df["PICS"].value_counts()
value_count_of_pics.plot()
plt.show()


print("#"*40, end="\n\n")
####################################
