from db import Base,engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship


#   Content <-o Contents o-o Report o-> Header

class Report(Base):
  __tablename__ = "report"
  reportid=Column(Integer, primary_key=True, index=True)
  username=Column(String(50))
  title = Column(String(255))
  teamid=Column(Integer)
  headerid = Column(Integer, ForeignKey('reportheader.headerid'))
  contentsid = Column(Integer, ForeignKey('reportcontents.contentsid'))
  timestamp=Column(DateTime)
  contents = relationship("ReportContents",back_populates="report")
  header = relationship("ReportHeader",back_populates="report")

class ReportHeader(Base):
  __tablename__="reportheader"
  headerid=Column(Integer, primary_key=True, index=True)
  type = Column(String(100))
  report=relationship("Report")

class ReportContents(Base):
  __tablename__="reportcontents"
  contentsid=Column(Integer, primary_key=True, index=True)
  report = relationship("Report",back_populates="contents")
  content = relationship("ReportContent",back_populates="contents")


class ReportContent(Base):
  __tablename__="reportcontent"
  contentid=Column(Integer, primary_key=True, index=True)
  contentsid = Column(Integer, ForeignKey('reportcontents.contentsid'))
  content=Column(String(600))
  contents=relationship("ReportContents",back_populates="content")
  
if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)



