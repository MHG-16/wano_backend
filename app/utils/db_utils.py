# -*- coding: utf-8 -*-
from werkzeug.local import LocalProxy
from flask import g

import mysql.connector as mariadb


def get_db():
    if "db" not in g:
        try:
            # pylint: disable=E0237
            g.db = connexion()
        except (ConnectionError) as err:
            raise ConnectionError("Problem connecting to database") from err
        return g.db
    return None


def connexion():
    return mariadb.connect(
        host="localhost",
        database="interface",
        user="MHG-16",
        password="password123",
        autocommit=True,
    )


def selectqueryfetchone(query):
    """nonbuffered query fetch"""
    try:
        datebase = LocalProxy(get_db)
        cursor = datebase.cursor()
        cursor.execute(query)
        column_value = cursor.fetchone()
        cursor.close()
        return column_value[0]
    except (IndexError, TypeError):
        return None
    except (ConnectionError) as err:
        raise ConnectionError("Problem connecting to database") from err


def updatequery(query: str):
    try:
        datebase = LocalProxy(get_db)
        cursor = datebase.cursor()
        cursor.execute(query)
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount > 0
    except (ConnectionError) as err:
        raise ConnectionError("Problem connecting to database") from err
