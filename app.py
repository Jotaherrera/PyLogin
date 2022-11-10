from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

# Flask App
app = Flask(__name__)
app.secret_key = b"\xfa\x1aX\x9eP\xb2\xff\x8c\xe9C\xf6R\x07\x05\xe7\x07"

# Database
client = pymongo.MongoClient("localhost", 27017)
db = client.py_login

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")

    return wrap


# Routes
from user import routes


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/account")
@login_required
def account():
    return render_template("account.html")
