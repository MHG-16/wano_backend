# -*- coding: utf-8 -*-
import traceback
from werkzeug.local import LocalProxy
from flask import g
import mysql.connector as mariadb
from sqlalchemy.exc import InterfaceError, OperationalError


def get_db():
    try:
        # pylint: disable=E0237
        g.db = connexion()
    except (ConnectionError) as err:
        raise ConnectionError("Problem connecting to database") from err
    return g.db


def connexion():
    return mariadb.connect(
        host="localhost",
        database="interface",
        user="MHG-16",
        password="password123",
        autocommit=True,
    )


def selectqueryfetchone(query: str) -> str:
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


def lastrowcolumnvalue(column_name: str, table_name: str) -> str:
    query = (
        f"SELECT {column_name} FROM {table_name} ORDER BY {column_name} DESC LIMIT 1"
    )
    return selectqueryfetchone(query)


def get_real_id(column_name: str, table_name: str, id_crypted: str) -> str:
    query = f"""SELECT {column_name}  FROM {table_name}
            where md5({column_name}) = '{id_crypted}'"""
    return selectqueryfetchone(query)


def check_get_real_id(column_name: str, table_name: str, id_crypted: str):
    real_id = get_real_id(column_name, table_name, id_crypted)
    if real_id is None:
        raise ValueError(f"Aucun {table_name} corresponds to id :{id_crypted}")
    return real_id


def selectquery(query):
    try:
        database = LocalProxy(get_db)
        cursor = database.cursor()
        cursor.execute(query)
        actions = cursor.fetchall()
        sequence = cursor.column_names
        result = [dict(zip(sequence, action)) for action in actions]
        cursor.close()
        return result
    except (InterfaceError, OperationalError) as err:
        raise ConnectionError("Connection  to database error") from err
    except TypeError:
        # query result is None => TypeError: zip argument #2 must support iteration
        return None


def updatequery(query: str):
    # pylint: disable=W0703
    try:
        datebase = LocalProxy(get_db)
        cursor = datebase.cursor()
        cursor.execute(query)
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount > 0
    except (ConnectionError) as err:
        raise ConnectionError("Problem connecting to database") from err
    except Exception:
        print(traceback.format_exc())
        return None
