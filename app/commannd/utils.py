# -*- coding: utf-8 -*-
from itertools import product
from sqlalchemy.exc import IntegrityError
from flask import jsonify

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
        SESSION.add(LigneDeCommand(**product, id_facture=id_facture))
    SESSION.commit()


def insert_command(data: dict):
    products = data.get("products")
    facture = data.get("facture")
    print(product)
    SESSION.add(Facture(**facture))
    SESSION.commit()
    insert_products(products)


def getRealIdEchennce(id_en_md5: str) -> int:
    return get_real_id("id_facture", "factures", id_en_md5)


def get_by_id(id_en_md5):
    query = f"""SELECT factures.date_facture, factures.id_kunde, factures.id_verkaufer,
    quantity, products.price as price_item, products.name   from ligneDeCommand
    INNER JOIN products ON products.id_product = ligneDeCommand.id_product
    INNER JOIN factures ON factures.id_facture = ligneDeCommand.id_facture
    where factures.id_facture = {id_en_md5}
    """
    row = selectquery(query)[0]

    row["client"] = get_full_name(row["id_kunde"])
    row["seller"] = get_full_name(row["id_verkaufer"])
    return row


def get_full_name(id_user):
    query = f"""SELECT concat(users.first_name, " ", users.last_name) AS full_name FROM users
            where id_user ={id_user}"""
    return selectqueryfetchone(query)
