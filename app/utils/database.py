# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    "mysql+mysqlconnector://MHG-16:password123@localhost/interface",
    pool_size=20,
    max_overflow=0,
    pool_recycle=3600,
)

SESSION = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
)

Base = declarative_base()


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
