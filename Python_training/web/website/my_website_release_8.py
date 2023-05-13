"""
added /validatelogin endpoint
"""

# --------------------
# html files
# --------------------
# - create directory called 'templates' inside 'website' directory
# - keep all html files inside 'templates'
# --------------------

# --------------------
# Create app for our website
# --------------------
import flask
my_website_app = flask.Flask(__name__)
# any name we can give, __name__ is builtin variable which is having value '__main__'
# --------------------


# --------------------
# END POINT-1: URL http://127.0.0.1:5000/ mapped to route('/')
# --------------------
# @my_website_app.route("/")
# def my_index_page():
#     return "Welcome"
# --------------------

# --------------------
# END POINT-2: URL http://127.0.0.1:5000/ mapped to route('/')
# --------------------
@my_website_app.route("/")
def my_index_page():
    return flask.render_template("index.html")
# --------------------


# --------------------
# END POINT-3: URL http://127.0.0.1:5000/about mapped to route('/about')
# --------------------
@my_website_app.route("/about")
def my_about_page():
    return flask.render_template("about.html")
# --------------------

# --------------------
# END POINT-4: URL http://127.0.0.1:5000/login mapped to route('/login')
# --------------------
@my_website_app.route("/login")
def my_login_page():
    return flask.render_template("login.html")
# --------------------

# --------------------
# END POINT-5: URL http://127.0.0.1:5000/register mapped to route('/register')
# --------------------
@my_website_app.route("/register")
def my_register_page():
    return flask.render_template("register.html")
# --------------------

# --------------------
# END POINT-6: URL http://127.0.0.1:5000/addnewuser mapped to route('/addnewuser')
# --------------------
@my_website_app.route("/addnewuser", methods=["POST"])
def my_addnewuser_page():
    """
    Our Plan
    Task-1: Get new user details
    Task-2: Check whether both passwords are matching
    Task-3: Create database & table
    Task-4: Check whether user already exists
    Task-5: Add new user
    """

    # --------------------
    # Task-1: Get new user details
    # --------------------
    # all form data will be automatically flask will capture
    #   and keep in a dictionary 'flask.request.form'
    entered_username = flask.request.form.get("uname") # uname is from register.html
    entered_password_1 = flask.request.form.get("pw1")
    entered_password_2 = flask.request.form.get("pw2")
    entered_email = flask.request.form.get("email")
    # --------------------

    # --------------------
    # Task-2: Check whether both passwords are matching
    # --------------------
    if entered_password_1 != entered_password_2:
        return "Both passwords should Match.<br><a href='/register'>Go Back</a>"
    # --------------------

    # --------------------
    # Task-3: Create database & table
    # --------------------
    import sqlite3

    print("Create/Connect to database 'my_users_db.sqlite'")
    my_db_connection = sqlite3.connect('my_users_db.sqlite')
    print("Done")

    print("Get the cursor object")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not present")
    my_query = '''
    CREATE TABLE IF NOT EXISTS MY_USERS_TABLE(
    NAME VARCHAR(100),
    PASSWORD VARCHAR(100),
    EMAIL VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # --------------------

    # --------------------
    # Task-4: Check whether user already exists
    # --------------------
    my_query = f"SELECT COUNT(*) FROM MY_USERS_TABLE WHERE NAME='{entered_username}'"
    my_db_cursor.execute(my_query)
    users_count = my_db_cursor.fetchone() # Ex: (10,)
    if users_count[0] > 0:
        return "User Already Exists.<br><a href='/register'>Go Back</a>"
    # --------------------

    # --------------------
    # Task-5: Add new user
    # --------------------
    my_query = f"INSERT INTO MY_USERS_TABLE VALUES('{entered_username}', '{entered_password_1}','{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "Account Created.<br><a href='/login'>Click Here To Login</a>"
    # --------------------

# --------------------

# --------------------
# END POINT-7: URL http://127.0.0.1:5000/validatelogin mapped to route('/validatelogin')
# --------------------
@my_website_app.route("/validatelogin", methods=["POST"])
def my_validatelogin():
    """
    Our Plan:
    Task-1: Get entered username and password
    Task-2: Validate with database
    Task-3: If login success then Display log data table content
    """
    # --------------------
    # Task-1: Get entered username and password
    # --------------------
    entered_username = flask.request.form.get("uname")
    entered_password = flask.request.form.get("pw")
    # --------------------

    # --------------------
    # Task-2: Validate with database
    # --------------------
    import sqlite3

    print("Create/Connect to database 'my_users_db.sqlite'")
    my_db_connection = sqlite3.connect('my_users_db.sqlite')
    print("Done")

    print("Get the cursor object")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    my_query = f"SELECT COUNT(*) FROM MY_USERS_TABLE WHERE NAME='{entered_username}' AND PASSWORD='{entered_password}'"
    my_db_cursor.execute(my_query)
    users_count = my_db_cursor.fetchone() # Ex: (10,)
    if users_count[0] == 0:
        return "Login Failed<br>User/Password didnt match.<br><a href='/register'>Go Back</a>"
    # --------------------

    # --------------------
    # Task-3: If login success then Display log data table content
    # --------------------
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
    return flask.render_template("log_report.html", my_data=my_db_result)
    # --------------------

# --------------------
# We can write python code inside 'html'
#   using below syntax
# --------------------
# - {%python_statement %} Use this for writing any python statement
#
# - {% if some_cond%} Use this syntax for any block
#    {%endif%}
#
# - {{varaible_name}} use this syntax to display python varaible
#
# - python code present inside html will be executed by the program
#   called 'TEMPLATE ENGINE'
#
# - Name of the 'TEMPLATE ENGINE' used in flask is 'JINJA2'
# --------------------

# --------------------

# --------------------
# Run builtin web server
# --------------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# --------------------
