from db import Base,engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship


class Report(Base):
  __tablename__ = "report"
  reportid=Column(Integer, primary_key=True, index=True)
  username=Column(String(50))
  title = Column(String(255))
  membersid=Column(Integer(100))
  headerid = Column(Integer, ForeignKey('reportheader.headerid'))
  contentsid = Column(Integer, ForeignKey('reportcontents.contentsid'))
  timestamp=Column(DateTime)

class ReportHeader(Base):
  __tablename__="reportheader"
  headerid=Column(Integer, primary_key=True, index=True)
  type = Column(String(100))
  reports=relationship("Report")

class ReportContent(Base):
  __tablename__="reportcontent"
  contentid=Column(Integer, primary_key=True, index=True)
  content=Column(String(600))
  
class Reportcontents(Base):
  __tablename__="reportcontents"
  contentsid=Column(Integer, primary_key=True, index=True)
  reports = relationship("ReportContents")




