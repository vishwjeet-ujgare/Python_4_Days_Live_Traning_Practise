"""
RESTFul web services using flask
"""

'''
Suppose we want provide access to log data table with others/public/other-application
How to share?/How to provide access?

OPTION-1: provide username, password, host, port, db name so that
public can access.

OPTION-1 will not be suitable for many reason including security 

OPTION-1 is like
our-application/our-DB   <----Direct Access----> others/public
'''

'''
We got 2 solutions
1) SOAP 2) REST
both tells dont use OPTION-1 instead introduce INTERFACE/GATE in between

now OPTION-2 is like
our-application/our-DB   <----INTERFACE/GATE----> others/public
This INTERFACE aslo called APPLICATION PROGRAMMING INTERFACE (API)

So, SOAP & REST are designs/architecture/style/tells-how-to-share

SOAP-API
REST-API

- REST came after SOAP
- REST is popular
- Compare to SOAP, REST is easy
'''

'''
I want to provide access my log data table using REST style architure,
how to write program or how to implement REST style architecture

Not required to implement from scracth
Becasue flask is already implemented REST architecture
'''

'''
Then how to create REST-API to provide access my log data table
using flask

- create app
- create endpoint
- pull data from db
- return data in json format
- run the server
- share ENPOINT with others/public so that they can access through that ENDPOINT
'''


# --------------------
# Create app for our log data REST-API
# --------------------
import flask
my_rest_api_app = flask.Flask(__name__)
# --------------------


# --------------------
# REST API END POINT: URL http://127.0.0.1:5000 mapped to route('/')
# --------------------
@my_rest_api_app.route("/")
def my_log_data_rest_api():
    """
    Our Plan:
    Create REST API for log data table so that we can provide
    access to others/public
    REST API END POINT: http://127.0.0.1:5000
    """

    import sqlite3

    print("Create/Connect to database 'my_data_db.sqlite'")
    my_db_connection = sqlite3.connect(r'../../programs/my_data_db.sqlite')
    print("Done")

    print("Get the cursor object")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    my_query = "SELECT * FROM MY_DATA_TABLE"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    my_db_result = dict(enumerate(my_db_result))
    # --------
    # Example:
    # --------
    # >>> L = [(),()]
    # >>> dict(enumerate(L))
    # {0: (), 1: ()}
    # >>>
    # --------

    return flask.jsonify(my_db_result)

# --------------------
# Run the server
# --------------------
my_rest_api_app.run()
# --------------------
