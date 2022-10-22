# -*- coding: utf-8 -*-
import os
from flask import request, jsonify
from flask import Blueprint

from app.commannd.utils import get_facture_pdf

from .utils import get_all_products, get_product, insert

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


@app.route("/product/get_by_id/<product_id>", methods=["GET"])
def get_product_by_id(product_id: str) -> dict:
    product = get_product(product_id)
    return jsonify({"error": False, "message": product}), 200


@app.route("/product/get_pdf/<id_product>")
def get_facture_in_pdf(id_product: str):
    pdf = get_facture_pdf(id_product)
    os.remove("facture.pdf")
    return pdf
