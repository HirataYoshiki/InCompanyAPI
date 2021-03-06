from sqlalchemy.sql.sqltypes import Boolean
from db import Base,engine
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
  userid = Column(Integer, primary_key=True, index=True)
  username = Column(String(50),nullable=False)
  password = Column(String(300),nullable=False)
  mailaddress = Column(String(100))
  editor = Column(Boolean,default=False)
  __tablename__ = "users"



if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)