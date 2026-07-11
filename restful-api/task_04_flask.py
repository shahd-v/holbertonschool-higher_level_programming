#!/usr/bin/python3
"""Provide a small RESTful API using Flask."""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Return a welcome message for the API root."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return the list of usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Return a simple health-check status message."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return one user's full data or a 404 error if missing."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from a JSON request body."""
    user = request.get_json(silent=True)

    if user is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user.get("username")
    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
