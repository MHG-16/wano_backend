# -*- coding: utf-8 -*-
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.utils.database import SESSION
from app.utils.db_utils import lastrowcolumnvalue, selectquery
from .models import Images, Products


def insert(data: dict):
    try:
        add_product(data)
    except IntegrityError:
        return jsonify({"error": True, "message": "user not found"}), 400
    except TypeError as err:
        return jsonify({"error": True, "message": str(err)}), 406
    insert_images(data["url_images"])
    return (jsonify({"error": False, "message": "user is created successfully"}), 200)


def insert_images(url_images: list) -> None:
    id_product = lastrowcolumnvalue("id_product", "products")
    for image in url_images:
        SESSION.add(Images(id_product=id_product, url_prefix=image))
    SESSION.commit()


def add_product(data: dict):
    product = Products(
        id_user=data["id_user"],
        name=data["name"],
        description=data["description"],
        price=data["price"],
        date_of_publish=data.get("date_of_publish", None),
    )
    SESSION.add(product)
    SESSION.commit()


def get_all_products():
    query = """SELECT products.*, GROUP_CONCAT(images.url_prefix SEPARATOR ',') AS url_images
    FROM products
    INNER JOIN images ON images.id_product = products.id_product  GROUP BY id_product """
    return selectquery(query)
