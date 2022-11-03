from flask import Flask, jsonify, request, session
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:
    def start_session(self, user):
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200

    def signUp(self):
        print(request.form)

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }

        # Password encryption
        user["password"] = pbkdf2_sha256.encrypt(user["password"])

        # Email check
        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            return jsonify(user), 200

        return jsonify({"error": "Sign up failed"}), 400
