# -*- coding: utf-8 -*-
from flask import request, jsonify

from app.run import app
from app.user.utils import insert, verify_existance_mail


@app.route("/user/create", methods=["POST"])
def create_user():
    data_user = request.json
    mail_user = data_user.get("email")
    print(verify_existance_mail(mail_user))
    if verify_existance_mail(mail_user):
        return (
            jsonify(
                {
                    "error": True,
                    "message": f"Il y a un compte avec cet addresse email:{mail_user}",
                }
            ),
            409,
        )
    response = insert(data_user)
    return response
