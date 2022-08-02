# -*- coding: utf-8 -*-
from flask import jsonify

from app.user.models import Users
from app.utils.database import SESSION


def insert(data: dict) -> dict:
    # pylint: disable=W0703
    try:
        user = Users(**data)
        SESSION.add(user)
        SESSION.commit()
    except Exception as err:
        return jsonify({"error": True, "message": str(err)}), 406
    return (jsonify({"error": False, "message": "user is created successfully"}),)


def verify_existance_mail(mail: str) -> bool:
    user = SESSION.query(Users).filter(Users.email == mail).first()
    return user is not None
