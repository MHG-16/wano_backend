# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify

from .utils import (
    get_all_data_factures,
    get_list_factures_by_id_client,
    insert,
    getRealIdEchennce,
)

app = Blueprint("Command Mangement API", __name__)


@app.route("/command/insert", methods=["POST"])
def insertproduct():
    try:
        data = request.get_json()
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
    facture = get_all_data_factures(id_facture)
    return jsonify({"error": False, "message": facture}), 200


@app.route("/command/list/<id_client>", methods=["GET"])
def get_list_all_of_factures_of_Client(id_client):
    if id_client is None:
        return (
            jsonify(
                {
                    "error": True,
                    "message": "Aucun facture not found in database with this id",
                }
            ),
            406,
        )
    factures = get_list_factures_by_id_client(id_client)
    return jsonify({"error": True, "message": factures}), 200
