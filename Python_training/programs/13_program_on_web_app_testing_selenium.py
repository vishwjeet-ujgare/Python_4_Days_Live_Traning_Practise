"""
selenium: Web application development

Test Case: Test whether google search is working or not.

Steps:
Step-1: open browser
Step-2: type the url
Step-3: findout search box
Step-4: type "Python"
Step-5: Press enter
Step-6: Check whether "Python" appears in browser title.
if found then test case success else test failed
"""
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

print("test case success")
print("Closing browser")
my_browser.close()

