from sqlalchemy.orm import backref
from sqlalchemy.sql.sqltypes import Boolean
from db import Base,engine
from sqlalchemy import Column, Integer, String, Boolean

class Character(Base):
  __tablename__="character"
  username=Column(String(50))
  


if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)