# -*- coding: utf-8 -*-
from flask import Blueprint

import app.user.views


app = Blueprint("Users API", __name__)
