# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

from .utils import insert, getRealIdEchennce, get_by_id

app = Blueprint("Command Mangement API", __name__)


@app.route("/command/insert", methods=["POST"])
def insertproduct():
    try:
        data = request.get_json()
        print(data)
    except TypeError:
        return jsonify({"error": True, "message": "Invalid parameters"}), 505
    return insert(data)


@app.route("/command/get_by_id/<id_facture>", methods=["GET"])
def get_facture_by_id(id_facture):
    id_facture = getRealIdEchennce(id_facture)
    if id_facture is None:
        return (
            jsonify(
                {
                    "error": True,
                    "message": "Aucun facture not found in database with this id",
                }
            ),
            406,
        )
    facture = get_by_id(id_facture)
    return jsonify({"error": False, "message": facture}), 200
