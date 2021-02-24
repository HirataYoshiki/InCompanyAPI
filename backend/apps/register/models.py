from db import Base,engine
from sqlalchemy import Boolean, Column, Integer, String, DateTime

class User(Base):
  userid = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  password = Column(String)
  mailaddress = Column(String)
  __tablename__ = "users"



if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)