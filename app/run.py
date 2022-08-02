# -*- coding: utf-8 -*-
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_marshmallow import Marshmallow

from .utils.database import SESSION, engine


app = Flask(__name__, template_folder="templates")
CORS(app)
ma = Marshmallow(app)


# Handling error
@app.errorhandler(Exception)
def _error(error):
    if isinstance(error, ConnectionError):
        return jsonify({"error": True, "message": str(error)}), 500

    if "405" in str(error):
        return jsonify({"error": True, "message": str(error)}), 405

    if "404" in str(error):
        return jsonify({"error": True, "message": str(error)}), 404

    return None


# start swagger specific #
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.yaml"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Seans-Python-Flask-REST-WanoAPIS"}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


# end swagger specific #


@app.teardown_request
def teardown_db(exception):
    # pylint: disable=unused-argument
    database = g.pop("db", None)
    if database is not None:
        database.close()
    if SESSION:
        SESSION.close()
        engine.dispose()
    # session_sql_alchemy.rollback()
