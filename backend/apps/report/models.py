from db import Base,engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Report(Base):
  __tablename__ = "report"
  username=Column(String(50))
  title = Column(String(255))
  membersid=Column(Integer(100))
  headerid = Column(Integer(100))
  contentsid = Column(Integer(100))
  timestamp=Column(DateTime)

class Header(Base):
  __tablename__="header"
  headerid=Column(Integer, primary_key=True, index=True)
  type = Column(String(100))
  





