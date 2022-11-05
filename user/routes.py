from flask import Flask
from app import app
from user.models import User


@app.route("/user/sign-up", methods=["POST"])
def signUp():
    return User().signUp()


@app.route("/user/sign-out")
def signOut():
    return User().singOut()


@app.route("/user/login", methods=["POST"])
def logIn():
    return User().logIn()
