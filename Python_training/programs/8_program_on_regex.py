"""
GEt data from web
and
extract using regular expression
"""

# --------------------
# Split into smaller
# --------------------
# Task-1: Get data from website using urllib-Keep it in variable
# Task-2: Extract log data using beautifulsoup
# Task-3: Extract info using regular expression
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
log_data = soup.body.pre.text
list_of_lines = log_data.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
####################################

print("# Task-3: Extract info using regular expression")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    # match_result = re.match('which pattern?', 'on which string')
    match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*',each_line)
    print("Each Line:", each_line)
    print("Match result:", match_result, end="\n\n")

# COMMENT - 2
'''
Regular Expression

# IDENTIFIERS
\d -> represents any one digit b/n 0-9
\D -> represents any one non-digit. except 0-9
. -> represent any ONE ANY character
\. -> represent strictly DOT
[.] -> represent strictly DOT
[0-9] -> represents any one digit b/n 0-9. Here we can specify range like 0-5

# QUANTIFIERS
\d{3} -> internally it will make \d\d\d
\d{1,3} -> internally it will make (\d|\d\d|\d\d\d)

# MOPDIFIERS
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 times
'''

# COMMENT - 1
'''
IP Address line pattern, 
which means we need to tell how ip address line looks like?

IP Address line looks like
FROM THE BEGINNING
1 to 3 digits then DOT
then
1 to 3 digits then DOT
then
1 to 3 digits then DOT
then
1 to 3 digits then SOME CHARACTERS PRESENT TILL THE END
'''

print("#"*40, end="\n\n")
####################################

print("Extract IP")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT
'''
- put () for ip address portion - called group
'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*'
- group number starting from 1
'''
print("#"*40, end="\n\n")
####################################

print("Extract IP, DATE")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
'''
26/Apr/2000

26
-------
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
[0-9]\d # Strictly 2 digits
\d[0-9] # Strictly 2 digits

\d{1,2} # minimum 1 digit, maximum 2
[0-9]{1,2} # minimum 1 digit, maximum 2
\d?\d # minimum 1 digit, maximum 2
[0-9]?[0-9] # minimum 1 digit, maximum 2
\d?[0-9] # minimum 1 digit, maximum 2
[0-9]?\d # minimum 1 digit, maximum 2
-------

Apr
-------
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
-------
'''

print("#"*40, end="\n\n")
####################################

print("Extract IP, DATE, PICS: PARTIAL OUTPUT - 1")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/pics/([0-9a-z]+\.(gif|jpg)).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(4)
        print(ip, dt, img)

# COMMENT
'''
\s -> one SPACE
\S -> any one character except SPACE
'''

print("#"*40, end="\n\n")
####################################

'''
-------
r[ea]d
-------
red
rad
-------

r[ea]{1,2}d
-------
red
rad
read
raed
-------

r[ea]+d
-------
red
rad
read
raed
-------

r[ea]*d
-------
rd
red
rad
read
raed
-------

r*d
-------
d
rd
rrd
rrrrd
-------


[r]*d
-------
d
rd
rrd
rrrrd
-------

r[ea]?d
-------
rd
red
rad
-------

'''

print("Extract IP, DATE, PICS")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img)

# COMMENT
'''
Make this "pics/wpaper.gif" portion optional so that it will match
the lines which is not having pics
 
(pics/([0-9a-z]+\.(gif|jpg)))?
'''

print("#"*40, end="\n\n")
####################################


print("Extract IP, DATE, PICS, URL")
print("-"*20)
# --------------------
import re
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[0-9a-zA-Z./_]+).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url)

# COMMENT
'''

http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

https? = s is optional
http[s]? = s is optional
(https)? = 'https' is optional

http[s]?://[0-9a-zA-Z./_]+
'''

print("#"*40, end="\n\n")
####################################

# BELOW CODE IS COPIED FROM PROGRAM-4
print("# Task-2: Create Empty files 'regex_report.txt' and 'regex_report.csv' with heading")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_txt_file_handle = open("regex_report.txt", "w")
my_csv_file_handle = open("regex_report.csv", "w")

# Step-2: Write Heading
# --------------------
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)


# Step-3: Disconnect
# --------------------
# We will close at the end

print("""
Files regex_report.txt and regex_report.csv
created with header, please check
""")

print("#"*40, end="\n\n")
####################################

print("Write to files")
print("-"*20)
# --------------------

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[0-9a-zA-Z./_]+).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url, sep="\t", file=my_txt_file_handle, flush=True)
        print(ip, dt, img, url, sep=",", file=my_csv_file_handle, flush=True)


my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Files regex_report.txt and regex_report.csv
created with data. Please check
""")

print("#"*40, end="\n\n")
####################################

