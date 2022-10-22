# -*- coding: utf-8 -*-
from sqlalchemy.exc import IntegrityError
from flask import jsonify, render_template, send_file
from pdfkit import from_string

from ..utils.db_utils import (
    lastrowcolumnvalue,
    get_real_id,
    selectquery,
    selectqueryfetchone,
)
from app.utils.database import SESSION
from .models import Facture, LigneDeCommand


def insert(data) -> dict:
    try:
        insert_command(data)
        return jsonify({"success": True, "message": "success"}), 200
    except IntegrityError:
        return (
            jsonify(
                {
                    "error": True,
                    "message": "client id or seller id or product or alles is not found",
                }
            ),
            400,
        )
    except TypeError:
        return (
            jsonify(
                {
                    "error": True,
                    "message": "parameter 'facture' or 'product' is not found",
                }
            ),
            400,
        )
    except Exception:
        return jsonify({"error": False, "message": "save on database failed"}), 505


def insert_products(data: list):
    id_facture = lastrowcolumnvalue("id_facture", "factures")
    for product in data:
        print(product["id_product"])
        product["id_product"] = get_real_id(
            "id_product", "products", product["id_product"]
        )
        SESSION.add(LigneDeCommand(**product, id_facture=id_facture))
    SESSION.commit()


def insert_command(data: dict):
    products = data.get("products")
    facture = data.get("facture")
    SESSION.add(Facture(**facture))
    SESSION.commit()
    insert_products(products)


def getRealIdEchennce(id_en_md5: str) -> int:
    return get_real_id("id_facture", "factures", id_en_md5)


def get_facture_by_id(id_en_md5):
    query = f"""SELECT factures.date_facture, factures.id_kunde AS id_client,
    CONCAT(users.last_name , " ", users.first_name ) AS client
    from factures INNER JOIN users ON users.id_user = factures.id_kunde
    where factures.id_facture = {id_en_md5}
    """
    return selectquery(query)[0]


def get_products_facture(id_facture):
    query = f"""SELECT quantity, products.name as product_name, CONCAT(users.last_name, " ", users.first_name ) AS vendor_name, products.price
    FROM ligneDeCommand
    INNER JOIN products ON products.id_product = ligneDeCommand.id_product
    INNER JOIN users ON users.id_user = products.id_user
    where id_facture ={id_facture}"""
    return selectquery(query)


def get_all_data_factures(id_facture: int) -> dict:
    facture = get_facture_by_id(id_facture)
    facture["products"] = get_products_facture(id_facture)
    return facture


def get_list_factures_by_id_client(id_client):
    query = f"SELECT id_facture FROM factures WHERE factures.id_kunde = {id_client}"
    return selectquery(query)


def get_full_name(id_user):
    query = f"""SELECT concat(users.first_name, " ", users.last_name) AS full_name FROM users
            where id_user ={id_user}"""
    return selectqueryfetchone(query)


def get_html_message_facture(data: dict) -> str:
    return f"""<div class="facureContent">
        <h1>{data["client"]}</h1>
        <h1>{data["date_facture"]}</h1>
    </div>
    """


def get_facture_pdf(id_en_md5: str):
    facture_data = get_all_data_factures(id_en_md5)
    rendred = render_template(
        "invoice.html",
        date_facture=facture_data["date_facture"],
        client_name=facture_data["client"],
        items=facture_data["products"],
    )
    from_string(rendred, "facture.pdf")
    return send_file("facture.pdf")
