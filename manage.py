# -*- coding: utf-8 -*-
# pylint: skip-file
from flask.cli import FlaskGroup
from app.utils.database import init_db, SESSION

from app import app


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    init_db()
    SESSION.commit()


if __name__ == "__main__":
    cli()
