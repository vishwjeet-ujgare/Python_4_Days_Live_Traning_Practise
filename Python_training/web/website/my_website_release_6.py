"""
added register.html
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
# Run builtin web server
# --------------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# --------------------
