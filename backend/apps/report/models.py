from db import Base,engine

from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from apps.report.scheme import ReportHeaderin, Reportupdate, Contentupdate


#   Content N-1 Contents 1-1 Report N-1 Header
class Report(Base):
  __tablename__ = "report"
  reportid=Column(Integer, primary_key=True, index=True)
  localreportid=Column(Integer,nullable=False)
  username=Column(String(50),nullable=False)
  title = Column(String(255),nullable=False)
  teamid=Column(Integer)
  headerid = Column(Integer, ForeignKey('reportheader.headerid'))
  contentsid = Column(Integer, ForeignKey('reportcontents.contentsid'))
  timestamp=Column(DateTime)
  contents = relationship("ReportContents",back_populates="report")
  header = relationship("ReportHeader",back_populates="report")

  def updates(self,updates:Reportupdate):
    for k,v in updates.__dict__.items():
      for sk in self.__dict__.keys():
        if k==sk and v!=None:
          setattr(self,sk,v)
    return self

class ReportHeader(Base):
  __tablename__="reportheader"
  headerid=Column(Integer, primary_key=True, index=True)
  localheaderid=Column(Integer)
  username=Column(String(50))
  type = Column(String(100),nullable=False)
  report=relationship("Report")

  def updates(self,updates:ReportHeaderin):
    for k,v in updates.__dict__.items():
      for sk in self.__dict__.keys():
        if k==sk and v != None:
          setattr(self,sk,v)
    return self

class ReportContentGroup(Base):
  __tablename__="reportcontentgroup"
  contentsid=Column(Integer, primary_key=True, index=True)
  localcontentsid=Column(Integer)
  username=Column(String(50))
  report = relationship("Report",back_populates="contents")
  content = relationship("ReportContent",back_populates="contents")


class ReportContent(Base):
  __tablename__="reportcontent"
  contentid=Column(Integer, primary_key=True, index=True)
  localcontentid=Column(Integer)
  username=Column(String(50))
  contentsid = Column(Integer, ForeignKey('reportcontentgroup.contentsid'))
  content=Column(String(600))
  contents=relationship("ReportContents",back_populates="content")

  def updates(self,updates:Contentupdate):
    for k,v in updates.__dict__.items():
      for sk in self.__dict__.keys():
        if k==sk and v!=None:
          setattr(self,sk,v)
    return self

if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)



