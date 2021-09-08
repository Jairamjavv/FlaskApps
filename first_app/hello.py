# importing flask class
from flask import Flask

'''
Creating an instance of Flask.
__name__ is a shortcut way to expose the application name. 
Flask uses this name to lookup the templates and static files.
'''
app = Flask(__name__)


'''
Flask's route() decorator tells what url to trigger. Here "/" is the root url.
This route url is added after the hosted url.

The function returns the content which will be displayed in the webpage.
'''
@app.route('/')
def hello_world():
    return "<h1>Hello Jairam</h1>"