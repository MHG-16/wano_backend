# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import Blueprint

from .utils import insert

app = Blueprint("Products API", __name__)


@app.route("/product/insert", methods=["POST"])
def create_product():
    try:
        data_prod = request.json
    except TypeError as err:
        return jsonify({"error": True, "message": err}), 405

    return insert(data_prod)
