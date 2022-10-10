# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import Blueprint

from .utils import get_all_products, insert

app = Blueprint("Products API", __name__)


@app.route("/product/insert", methods=["POST"])
def create_product():
    try:
        data_prod = request.json
    except TypeError as err:
        return jsonify({"error": True, "message": err}), 405

    return insert(data_prod)


@app.route("/product/list", methods=["GET"])
def get_list_all_of_products():
    products = get_all_products()
    return jsonify({"error": False, "message": {"products": products}}), 200
