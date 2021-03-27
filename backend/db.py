import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

url = config.Develop.config["DB_URL"]

engine = sqlalchemy.create_engine(url, echo=True)
SessionLocal = sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
    )

def get_session():
    db = SessionLocal() # sessionを生成
    try:
        yield db
    finally:
        db.close()

Base=declarative_base()