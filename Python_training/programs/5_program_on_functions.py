"""
Write a function to process log file

If we pass log file path then function should extract info and
return extracted info

-----------------
Expected return value:
-----------------
[
(123.123.123.123,wpaper.gif),
(123.123.123.123,No Image),
(123.123.123.123,5star2000.gif),
(123.123.123.123,5star.gif),
(123.123.123.123,a2hlogo.gif),
(123.123.123.123,No Image)
]
-----------------

"""


def log_process_func_pos_arg(log_file_path):
    """
    This function will receive log file path, extract info
    and send extracted info
    :param log_file_path:
    :return list_of_tuples:
    """
    # --------------------
    # Get data from log file
    # --------------------
    my_log_file_handle = open(log_file_path, "r")
    list_of_lines = my_log_file_handle.readlines()
    my_log_file_handle.close()
    # --------------------

    # --------------------
    # Extract Info
    # --------------------
    final_result = []
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
            each_line_data = (ip, img)
            final_result.append(each_line_data)
    return final_result
    # --------------------


def log_process_func_kw_arg(*, log_file_path):
    """
    This function will receive log file path, extract info
    and send extracted info
    :param log_file_path:
    :return list_of_tuples:
    """
    # --------------------
    # Get data from log file
    # --------------------
    my_log_file_handle = open(log_file_path, "r")
    list_of_lines = my_log_file_handle.readlines()
    my_log_file_handle.close()
    # --------------------

    # --------------------
    # Extract Info
    # --------------------
    final_result = []
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
            each_line_data = (ip, img)
            final_result.append(each_line_data)
    return final_result
    # --------------------


func_result_1 = log_process_func_pos_arg("../log/server_log.txt")
print("func_result_1:", func_result_1, end="\n\n")

func_result_2 = log_process_func_kw_arg(log_file_path="../log/server_log.txt")
print("func_result_2:", func_result_2, end="\n\n")
