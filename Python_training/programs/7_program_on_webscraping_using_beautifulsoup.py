"""
Webscraping using beautifulsoup

Extract log data from web
"""

# --------------------
# Split into smaller
# --------------------
# Task-1: Get data from website using urllib-Keep it in variable
# Task-2: Extract info using beautifulsoup
# --------------------

print("# Task-1: Get data from website using urllib-Keep it in variable")
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

web_content = web_content.decode()
print(web_content)

print("#"*40, end="\n\n")
####################################

print("# Task-2: Extract info using beautifulsoup")
print("-"*20)
# --------------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
print(soup)

print("#"*40, end="\n\n")
####################################

print("Methods inside 'bsoup' class")
print("-"*20)
# --------------------

print(dir(soup))

print("#"*40, end="\n\n")
####################################

print("Head tag")
print("-"*20)
# --------------------

print(soup.head)

print("#"*40, end="\n\n")
####################################

print("Title tag")
print("-"*20)
# --------------------

print(soup.head.title) # <TITLE>A Web server log file explained</TITLE>

print("#"*40, end="\n\n")
####################################


print("Title tag text")
print("-"*20)
# --------------------

print(soup.head.title.text) # A Web server log file explained

print("#"*40, end="\n\n")
####################################

print("1st link tag")
print("-"*20)
# --------------------

print(soup.head.link) # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">

print("#"*40, end="\n\n")
####################################

print("all link tags")
print("-"*20)
# --------------------

print(soup.head.find_all('link'))

print("#"*40, end="\n\n")
####################################

print("log data")
print("-"*20)
# --------------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
####################################

print("log data in raw format")
print("-"*20)
# --------------------

print(repr(log_data))

print("#"*40, end="\n\n")
####################################

print("list of lines")
print("-"*20)
# --------------------

list_of_lines = log_data.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
####################################

# BELOW CODE IS COPIED FROM PROGRAM-4
print("# Task-2: Create Empty files 'web_report.txt' and 'web_report.csv' with heading")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_txt_file_handle = open("web_report.txt", "w")
my_csv_file_handle = open("web_report.csv", "w")

# Step-2: Write Heading
# --------------------
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)


# Step-3: Disconnect
# --------------------
# We will close at the end

print("""
Files web_report.txt and web_report.csv
created with header, please check
""")

print("#"*40, end="\n\n")
####################################

print("Write to files")
print("-"*20)
# --------------------

for each_line in list_of_lines:
    if each_line.startswith("123"):
        sp = each_line.split()
        ip = sp[0]
        raw_img = sp[6]
        # if raw_img.endswith("jpg") or raw_img.endswith("png") or raw_img.endswith("gif")
        # OR
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"
        print(ip, img, sep="\t", file=my_txt_file_handle, flush=True)
        print(ip, img, sep=",", file=my_csv_file_handle, flush=True)

my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Files web_report.txt and web_report.csv
created with data. Please check
""")

print("#"*40, end="\n\n")
####################################
