# -*- coding: utf-8 -*-
from app.user.models import Users
from app.utils.database import SESSION


def insert(data: dict):
    user = Users(**data)
    SESSION.add(user)
    SESSION.commit()
