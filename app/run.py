# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)

# Handling error
@app.errorhandler(Exception)
def _error(error):
    if isinstance(error, ConnectionError):
        return jsonify({"error": True, "message": str(error)}), 500

    if 405 in str(error):
        return jsonify({"error": True, "message": str(error)}), 405

    if 404 in str(error):
        return jsonify({"error": True, "message": str(error)}), 404

    return None
