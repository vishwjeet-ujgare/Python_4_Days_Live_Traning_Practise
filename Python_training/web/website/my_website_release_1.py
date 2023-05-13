"""
Python for web development

We have many web development frameworks
- bottle framework : Micro & production frameworks only
- flask framework : Micro & production frameworks only
- django framework : MVT(Model View Templete) -> Highly scable application
- web2py framework : MVC
- pyramid framework: MVC
- falcon framework : Micro
- fastapi framework : Micro
Many More
"""

'''
We are discussing
flask framework
'''

'''
To run any web application,
we need 
1) web server: flask has builtin server(development purpose)
2) database: sqlite
3) browser
'''

'''
Using flask,
1. We can develop websites
2. We can develop RESTFul web service like REST-API, Micro services
'''

'''
Here we are discussing
1. We can develop websites
'''

# --------------------
# Create app for our website
# --------------------
import flask
my_website_app = flask.Flask(__name__)
# any name we can give, __name__ is builtin variable which is having value '__main__'
# --------------------

# EMPTY WEBSITE, No Pages Created

# --------------------
# Run builtin web server
# --------------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# --------------------
