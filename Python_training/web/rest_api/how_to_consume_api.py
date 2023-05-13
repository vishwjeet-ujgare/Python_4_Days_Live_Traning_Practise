"""
Consume API using 'requests' module
"""


print("Access log data api and print the data")
print("-"*20)
# --------------------

import requests

api_response = requests.get("http://127.0.0.1:5000")
api_response = api_response.json()
print("api_response:", api_response)


print("#"*40, end="\n\n")
####################################

print("Access log data api and print the data")
print("-"*20)
# --------------------

import pandas as pd

my_rest_api_data_df = pd.DataFrame(api_response,index=["IP", "DATE", "PICS", "URL"])
my_rest_api_data_df = my_rest_api_data_df.T # Convert rows to columns
my_rest_api_data_df.to_csv("rest_api_data.csv")
my_rest_api_data_df.to_excel("rest_api_data.xlsx")
my_rest_api_data_df.to_json("rest_api_data.json")

print("""
Files created with REST API data
Please check 
rest_api_data.csv
rest_api_data.xlsx
rest_api_data.json
""")

print("#"*40, end="\n\n")
####################################

print("Access Weather API with dummy data")
print("-"*20)
# --------------------
import requests
weather_api_response = requests.get("https://demoqa.com/utilities/weather/city/pune")
weather_api_response = weather_api_response.json()
print(weather_api_response)

print("#"*40, end="\n\n")
####################################
