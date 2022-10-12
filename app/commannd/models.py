# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..utils.database import Base


class Facture(Base):
    # pylint: disable=R0902
    __tablename__ = "factures"

    id_facture = Column(Integer, primary_key=True)
    date_facture = Column(String(10), default=datetime.now().strftime("%Y-%m-%d"))
    id_verkaufer = Column(Integer, ForeignKey("users.id_user"))
    verkaufer = relationship(
        "Users", primaryjoin="Users.id_user == Facture.id_verkaufer"
    )
    id_kunde = Column(Integer, ForeignKey("users.id_user"))
    kunde = relationship("Users", primaryjoin="Users.id_user == Facture.id_kunde")

    def __init__(
        self, id_facture=None, date_facture=None, id_verkaufer=None, id_kunde=None
    ):
        self.id_facture = id_facture
        self.date_facture = date_facture
        self.id_kunde = id_kunde
        self.id_verkaufer = id_verkaufer

    def get_by_id_verkaufer(self):
        pass

    def get_by_intervalDate(self):
        pass

    def remove(self):
        pass


class LigneDeCommand(Base):
    # pylint: disable=R0902
    __tablename__ = "ligneDeCommand"
    id_cmd = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False, default=0)
    id_facture = Column(Integer, ForeignKey("factures.id_facture"), nullable=False)
    facture = relationship(
        "Facture", primaryjoin="Facture.id_facture == LigneDeCommand.id_facture"
    )
    id_product = Column(Integer, ForeignKey("products.id_product"), nullable=False)
    product = relationship(
        "Products", primaryjoin="Products.id_product == LigneDeCommand.id_product"
    )

    def __init__(self, quantity=None, id_product=None, id_facture=None):
        self.quantity = quantity
        self.id_product = id_product
        self.id_facture = id_facture

    def getTotalCost(self):
        pass

    def insert(self):
        pass

    def get(self):
        pass

    def remove(self):
        pass
