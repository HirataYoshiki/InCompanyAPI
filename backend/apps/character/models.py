from db import Base,engine
from sqlalchemy import Column, String, Integer

class Character(Base):
  __tablename__ = "character"
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50))
  department = Column(String(50))
  position = Column(String(50))
  # skills would be List -> String when insert
  skills = Column(String(300))




if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)