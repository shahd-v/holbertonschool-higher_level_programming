#!/usr/bin/python3
"""Provide a Flask API with Basic authentication and JWT protection."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-this-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify Basic authentication credentials."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Return a consistent Basic authentication error response."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Return a 401 response when a JWT is missing."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Return a 401 response when a JWT is invalid."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(*args):
    """Return a 401 response when a JWT has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(*args):
    """Return a 401 response when a JWT has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(*args):
    """Return a 401 response when a fresh JWT is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a protected message for valid Basic auth credentials."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT access token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a protected message for valid JWT credentials."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return an admin-only message for users with the admin role."""
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
