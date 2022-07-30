# -*- coding: utf-8 -*-
# pylint: disable=R0903
from sqlalchemy import Column, Integer, String, Date
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..utils.database import Base


class Users(Base):
    # pylint: disable=R0902
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    last_name = Column(String(25), nullable=False)
    first_name = Column(String(25), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    tel = Column(String(25), nullable=False)
    user_status = Column(Integer, nullable=False)

    def __init__(
        self,
        id_user=None,
        last_name=None,
        first_name=None,
        email=None,
        password=None,
        date_of_birth=None,
        tel=None,
        user_status=None,
    ):
        # pylint: disable=R0913
        self.id_user = id_user
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.tel = tel
        self.user_status = user_status


class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
