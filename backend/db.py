import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

url = config.Develop.config["DB_URL"]

engine = sqlalchemy.create_engine(url, echo=True)
Session = sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
    )

def get_session():
    try:
        SessionLocal = Session() # sessionを生成
        return SessionLocal
    finally:
        SessionLocal.close()

Base=declarative_base()