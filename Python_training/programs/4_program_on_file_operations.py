"""
Get data from server_log.txt, and
extract
IP
PICS
from each IP address lines
and
write extracted data to 'log_report.txt' and 'log_report.csv'

-----------------
Expected Output in log_report.txt:
-----------------
123.123.123.123     wpaper.gif
123.123.123.123     No Image
123.123.123.123     5star2000.gif
123.123.123.123     5star.gif
123.123.123.123     a2hlogo.gif
123.123.123.123     No Image
-----------------

-----------------
Expected Output in log_report.csv:
-----------------
123.123.123.123,wpaper.gif
123.123.123.123,No Image
123.123.123.123,5star2000.gif
123.123.123.123,5star.gif
123.123.123.123,a2hlogo.gif
123.123.123.123,No Image
-----------------

"""

# -----------------
# Split into smaller tasks
# -----------------
# Task-1: Get data from server_log.txt & keep it in a 'list' variable
# Task-2: Create Empty files 'log_report.txt' and 'log_report.csv' with heading
# Task-3: Extract Info  Write to files 'log_report.txt' and 'log_report.csv'
# -----------------

print("# Task-1: Get data from server_log.txt & keep it in a 'list' variable")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_log_file_handle = open("../log/server_log.txt", "r")

# Step-2: Read
# --------------------
list_of_lines = my_log_file_handle.readlines()

# Step-3: Disconnect
# --------------------
my_log_file_handle.close()

print(list_of_lines)

print("#"*40, end="\n\n")
####################################

print("# Task-2: Create Empty files 'log_report.txt' and 'log_report.csv' with heading")
print("-"*20)
# --------------------

# Step-1: Connect to file
# --------------------
my_txt_file_handle = open("log_report.txt", "w")
my_csv_file_handle = open("log_report.csv", "w")

# Step-2: Write Heading
# --------------------
# write heading to txt file
# my_txt_file_handle.write("IP\tPICS\n")
# my_txt_file_handle.writelines(["IP\t", "PICS\n"])
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)

# write heading to csv file
# my_csv_file_handle.write("IP,PICS\n")
# my_csv_file_handle.writelines(["IP,", "PICS\n"])
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)


# Step-3: Disconnect
# --------------------
# We will close at the end

print("""
Files log_report.txt and log_report.csv
created with header, please check
""")

print("#"*40, end="\n\n")
####################################

print("# Task-3: Extract Info  Write to files 'log_report.txt' and 'log_report.csv'")
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
Files log_report.txt and log_report.csv
created with data. Please check
""")

print("#"*40, end="\n\n")
####################################
