from flask import Flask, request
from markupsafe import escape   

app = Flask(__name__)

# url: 127.0.0.1:5000/
@app.route('/')
def first():
    return '<h1>First Page</h1>'

# url: 127.0.0.1:5000/second
@app.route('/second')
def second():
    return '<h1>Second Page</h1>'
    
# url: 127.0.0.1:5000/third
@app.route('/third')
def third():
    return '<h1>Third Page</h1>'

# passing variables over the URL.
# example-URL: 127.0.0.1:5000/'Good Morning
@app.route('/<greet>')
def greet_function(greet):
    return f'<h1>This page greets you</h1><br><h2>{escape(greet)}<h2>'

# passing the variables with datatypes specified
# example-URL: 127.0.0.1:5000/102/'Jairam'/89.0
@app.route('/<int:id>/<string:name>/<float:marks>')
def profile(id, name, marks):
    return f'<p>{name} with {id} got marks: {marks}</p>'


# handling POST or GET requests (Simple example)
@app.route('/login', methods=['GET', 'POST'])
def post_get():
    if request.method == 'POST':
        return '<h1>THIS IS FROM POST</h1>'
    else:
        return '<h1>THIS IS FROM GET</h1>'