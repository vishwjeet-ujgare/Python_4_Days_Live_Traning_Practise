"""
pytest for unittesting: to execute multiple test cases

Steps:
- file name should starts with test_
- write function for each test
- function name should also startswith test_
- validate result using assert
"""

# Test Case - 1:
def test_add_test():
    a = 10
    b = 20
    c = a + b
    assert b > 10
    assert c == 30

# Test Case - 2:
from mymodule import location, log_process_func_kw_arg
def test_mymodule_location():
    assert location == "India"

# Test Case - 3:
def test_mymodule_log_func():
    log_result = log_process_func_kw_arg(log_file_path="../log/server_log.txt")
    assert len(log_result) > 1
    assert type(log_result).__name__ == 'list'
    assert type(log_result[0]).__name__ == "tuple"
    # Example:
    # >>> a = 10
    # >>> type(a)
    # <class 'int'>
    # >>> type(a).__name__
    # 'int'

# Test Case 4:
def test_google_search():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    # Step-1: open browser
    my_browser = webdriver.Chrome()

    # Step-2: type the url
    my_browser.get("https://www.google.com")

    # Step-3: findout search box
    google_search_field = my_browser.find_element(by="name", value="q")

    # Step-4: type "Python"
    google_search_field.send_keys("Python")

    # Step-5: Press enter
    google_search_field.send_keys(Keys.RETURN)

    # Step-6: Check whether "Python" appears in browser title.
    # if found then test case success else test failed

    # instead of if-else, we will use assert to check the result
    # assert will throw error if condition fails
    assert "Python" in my_browser.title


# Command to execute test
# pytest -v .\test_pytest_example.py

