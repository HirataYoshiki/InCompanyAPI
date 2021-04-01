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
  localgroupid = Column(Integer, ForeignKey('reportcontentgroup.groupid'))
  timestamp=Column(DateTime)
  group = relationship("ReportContentGroup")
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
  groupid=Column(Integer, primary_key=True, index=True)
  username=Column(String(50))
  localgroupid=Column(Integer)
  contentid=Column(Integer,ForeignKey('reportcontent.contentid'))
  order=Column(Integer)
  report = relationship("Report")
  content = relationship("ReportContent")

class ReportContent(Base):
  __tablename__="reportcontent"
  contentid=Column(Integer, primary_key=True, index=True)
  localcontentid=Column(Integer)
  username=Column(String(50))
  content=Column(String(600))

  def updates(self,updates:Contentupdate):
    for k,v in updates.__dict__.items():
      for sk in self.__dict__.keys():
        if k==sk and v!=None:
          setattr(self,sk,v)
    return self

if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)



