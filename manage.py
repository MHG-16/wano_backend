# -*- coding: utf-8 -*-
# pylint: skip-file
from flask.cli import FlaskGroup

from app import app


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
