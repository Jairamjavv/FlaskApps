from flask import Flask

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