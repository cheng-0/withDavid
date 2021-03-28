from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'goodbye world\n'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username, password = data['username'], data['password']

    print(f'username: {username}; password: {password};')

    return f'hello {username}\n'


app.run(host='0.0.0.0', port=3000)
