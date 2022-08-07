# -*- coding: utf-8 -*-
from flask import jsonify, request, Blueprint

from app.auth.utils import verify_email_and_password


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
