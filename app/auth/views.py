# -*- coding: utf-8 -*-
from flask import jsonify, request, Blueprint

from app.auth.utils import verify_email_and_password, update_token_by_access_token


app = Blueprint("auth API", __name__)


@app.route("/login", methods=["POST"])
def login():
    email = password = None
    if request.authorization:
        email = request.authorization.get("username")
        password = request.authorization.get("password")
        return verify_email_and_password(email, password)
    return (
        jsonify({"error": True, "message": "email and password are required"}),
        400,
    )


@app.route("/logout", methods=["POST"])
def logout():
    id_session = request.headers.get("authorization")
    response = update_token_by_access_token(id_session)
    print(id_session)
    if response:
        return jsonify({"error": False, "message": "user is logged out"}), 200
    return jsonify({"error": True, "message": "idSession not found"}), 405
