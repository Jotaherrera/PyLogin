from flask import Flask
from app import app
from user.models import User


@app.route("/sign-up", methods=["POST"])
def signUp():
    return User().signUp()


@app.route("/sign-out")
def signOut():
    return User().singOut()


@app.route("/log-in", methods=["POST"])
def logIn():
    return User().logIn()
