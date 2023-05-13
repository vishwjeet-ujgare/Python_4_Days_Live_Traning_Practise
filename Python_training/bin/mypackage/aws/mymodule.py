"""
In this file we are keeping
Variables, Functions & classes
which we need to use it in more than one program

This file also called as "PYTHON MODULE" or "PYTHON LIBRARY"
"""

location = "India"

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
