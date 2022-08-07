# -*- coding: utf-8 -*-
from flask import jsonify
from app.utils.auth_utils import check_login_by_email


def verify_email_and_password(email: str, password: str):
    login = check_login_by_email(email, password)
    if login == -1:
        return jsonify({"error": True, "message": "Unkown email"}), 400
    if login == 1:
        return jsonify({"error": False, "message": "Success"}), 200
    return jsonify({"error": False, "message": "Password is incorrect"}), 400
