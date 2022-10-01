# -*- coding: utf-8 -*-
# pylint: skip-file
from flask.cli import FlaskGroup
from contextlib import suppress
from app.products.models import Products

from app.run import app
from app.user.models import Users
from app.utils.database import SESSION, engine


def init_db():
    with suppress(Exception):
        Users.__table__.drop(engine)
        Products.__table__.drop(engine)
    Users.__table__.create(engine)
    Products.__table__.create(engine)


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    init_db()
    SESSION.commit()


if __name__ == "__main__":
    cli()
