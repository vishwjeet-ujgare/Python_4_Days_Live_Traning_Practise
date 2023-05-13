"""
From the below string,
extract
IP
PICS
from each IP address lines
-----------------
Expected Output:
-----------------
123.123.123.123     wpaper.gif
123.123.123.123     No Image
123.123.123.123     5star2000.gif
123.123.123.123     5star.gif
123.123.123.123     a2hlogo.gif
123.123.123.123     No Image
-----------------

"""

print("How input data looks like?")
print("-"*20)
# --------------------

in_string = '''
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
'''

print(in_string)

print("#"*40, end="\n\n")
####################################

print("How input data looks like in RAW FORMAT?")
print("-"*20)
# --------------------

print(repr(in_string))

print("#"*40, end="\n\n")
####################################

print("What type of data we are receiving?")
print("-"*20)
# --------------------

print(type(in_string))

print("#"*40, end="\n\n")
####################################

print("Methods inside the str class which we can make use to get output")
print("-"*20)
# --------------------

print(dir(in_string))

print("#"*40, end="\n\n")
####################################

print("Separateout each line")
print("-"*20)
# --------------------

list_of_lines = in_string.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
####################################

print("print each line")
print("-"*20)
# --------------------

for each_line in list_of_lines:
    print("Each Line:", each_line)

print("#"*40, end="\n\n")
####################################

print("print each IP Address line")
print("-"*20)
# --------------------

for each_line in list_of_lines:
    if each_line.startswith("123"):
        print("Each Line:", each_line)

print("#"*40, end="\n\n")
####################################

print("print each IP Address line")
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
        print(ip, img, sep="\t")

print("#"*40, end="\n\n")
####################################
