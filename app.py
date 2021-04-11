from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from skAPI import login2 as skLogin
import asyncio
from threading import Thread


app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def login():
    print("start")
    if request.method == "POST":
        print("post")
        username = request.form['username']
        print(f"({username})")
        password = request.form['password']
        print(type(username))
        new_thread = Thread(target=skLogin.login4, args = (username, password))
        new_thread.start()
        new_thread.join()
        print("nice")
        if True:
            return redirect(url_for("menu", usr = username))
        return render_template('login.html')
    else:
        print("get")
        return render_template('login.html')

@app.route('/menu<usr>')
def menu(usr):
    return render_template('menu.html', username = usr)

@app.route('/setmodol')
def setModel():
    return render_template('setModol.html')

@app.route('/workingmodol')
def workingModel():
    return render_template('workingModol.html')

if __name__ == "__main__":
    # skLogin.login4(pw.username, pw.password)
    app.run(debug=True)