# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship, backref

from ..utils.gen_utils import validate_format_date
from ..utils.database import Base


class Products(Base):
    # pylint: disable=R0902
    __tablename__ = "products"

    id_product = Column(Integer, primary_key=True, nullable=False)
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    user = relationship("Users", backref=backref("products"))
    name = Column(String(25), nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    date_of_publish = Column(
        String(10), nullable=False, default=datetime.now().strftime("%Y-%m-%d")
    )
    description = Column(String(255))

    # pylint: disable=R0913
    def __init__(
        self,
        id_product=None,
        id_user=None,
        name=None,
        price=None,
        date_of_publish=None,
        description=None,
    ):
        self.id_product = id_product
        self.id_user = id_user
        self.name = name
        self.price = price
        self.date_of_publish = (
            validate_format_date(date_of_publish, "%Y-%m-%d")
            if date_of_publish
            else None
        )
        self.description = description

    def update(self, data: dict):
        pass

    def get(self):
        pass


class Images(Base):
    # pylint: disable=R0902
    __tablename__ = "images"

    id_image = Column(Integer, primary_key=True, nullable=False)
    id_product = Column(Integer, ForeignKey("products.id_product"), nullable=False)
    product = relationship("Products", backref="images")
    url_prefix = Column(String(255), nullable=False)

    def __init__(self, id_image=None, id_product=None, url_prefix=None):
        self.id_image = id_image
        self.id_product = id_product
        self.url_prefix = url_prefix

    def delete(self):
        pass

    def delete_all(self):
        pass
