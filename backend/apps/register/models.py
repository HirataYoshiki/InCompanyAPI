from db import Base,engine
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
  userid = Column(Integer, primary_key=True, index=True)
  username = Column(String(50))
  password = Column(String(300))
  mailaddress = Column(String(100))
  __tablename__ = "users"



if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)