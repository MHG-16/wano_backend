# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from utils.constants import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0, pool_recycle=3600
)

SESSION = scoped_session(
    sessionmaker(autocommit=False, autoFlash=False, bind=engine, expire_on_commit=False)
)

Base = declarative_base()


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
