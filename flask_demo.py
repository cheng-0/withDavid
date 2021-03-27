from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return 'goodbye world\n'


@app.route('/ticker')
def ticker():
    return '\n'.join(['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOG'])


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f'username: {username}; password: {password};')
    return f'hello {username}'


app.run(host='0.0.0.0', port=3000)
