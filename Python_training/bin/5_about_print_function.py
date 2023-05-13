"""
About print function
"""

print("About print function PART-1")
print("-"*20)
# --------------------

a = 100
b = 200
c = 300
d = 400

print(a,b,c,d)
# By default sep=SPACE, In output, print each value separated by SPACE

print(a,b,c,d, sep=",")
# In output, print each value separated by COMMA

print(a,b,c,d, sep="|")
# In output, print each value separated by PIPE

print(a,b,c,d, sep="XYZ")
# In output, print each value separated by XYZ

print("#"*40, end="\n\n")
####################################


print("About print function PART-2")
print("-"*20)
# --------------------

a = 100
b = 200
c = 300
d = 400

print(a,b,c,d) # by default end="\n". after printing all the values, put "\n" at the end
print(a,b,c,d, end=".") # end="." after printing all the values, put "." at the end
print(a,b,c,d, end="XYZ") # end="XYZ" after printing all the values, put "XYZ" at the end
print(a,b,c,d, end="ABC\n") # end="ABC\n" after printing all the values, put "ABC\n" at the end

# Total 4 args we can pass to print : 1) sep 2) end 3) file 4) flush
# Refer file operations example for file& flush

print("#"*40, end="\n\n")
####################################
