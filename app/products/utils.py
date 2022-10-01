# -*- coding: utf-8 -*-
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.utils.database import SESSION
from .models import Images, Products


def insert(data: dict):
    try:
        add_product(**data)
    except IntegrityError:
        return jsonify({"error": True, "message": "user not found"}), 400
    except TypeError as err:
        return jsonify({"error": True, "message": str(err)}), 406
    return (jsonify({"error": False, "message": "user is created successfully"}), 200)


def insert_images(nb_images: int, id_product) -> None:
    for _ in range(nb_images):
        SESSION.add(Images(id_product=id_product))
    SESSION.commit()


def add_product(data: dict):
    product = Products(
        id_user=data["id_user"],
        name=data["name"],
        description=data["description"],
        price=data["price"],
        date_of_publish=data["date_of_publish"],
    )
    SESSION.add(product)
    SESSION.commit()
