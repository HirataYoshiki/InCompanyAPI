from db import get_session
from apps.report.models import Report,ReportHeader
from apps.report.scheme import ReportHeaderin, ReportHeaderout, Reportin,Reportupdate, Reportout
from apps.register.models import User
from auth import get_current_user

from fastapi import Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session, Query
from pydantic.error_wrappers import ValidationError
from starlette.status import HTTP_400_BAD_REQUEST

from typing import Optional


# For report: POST Method-------------------------------------------------------
async def create_new_report(
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session),
  input:Reportin=Depends()):

  q = session.query(Report).filter(
    Report.username==current_user.username).order_by(
      desc(Report.reportid)
      ).first()
  try:
    localreportid:int= q.localreportid +1
  except:
    #for the first post
    localreportid=1
  adds = Report(
    **input.__dict__,
    username=current_user.username,
    localreportid = localreportid)
  session.add(adds)
  try:
    session.commit()
    report = session.query(Report).filter(
      Report.username==current_user.username,
      Report.localreportid==localreportid
      ).one()
    return Reportout(**report.__dict__)
  except Exception as e:
    print(e)
    session.rollback()
    return {"status":False}


#--------------------------------------------------------------------------------------

async def get_current_users_reports(
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)
  ):
  try:
    query:Query = session.query(Report).filter(Report.username==current_user.username)
    return query
  except:
    print("Error: control.py")
    return None

async def get_current_users_reports_by_id(
  reportid:int,
  query: Query = Depends(get_current_users_reports)
  ):
  result:Report = query.filter(Report.reportid==reportid).one()
  report = Reportout(**result.__dict__)
  return report
#--------------------------------------------------------------------------------------
async def update_current_users_reports_by_id(
  localreportid:int,
  update:Reportupdate=Depends(),
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session) 
):
  report:Report = session.query(Report).filter(
    Report.username==current_user.username,
    Report.localreportid==localreportid
    ).one()
  
  updated:Report=report.updates(update)
  copy= updated.__dict__.copy()
  session.commit()
  print(copy)
  return Reportout(**copy)



async def create_new_header(
  header:ReportHeaderin=Depends(),
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)):

  adds = ReportHeader(**header.__dict__)
  session.add(adds)
  session.commit()

  reportheader = ReportHeaderout(
    **session.query(ReportHeader).order_by(desc(ReportHeader.headerid)).first().__dict__
  )
  return reportheader


async def get_header_query(
  session:Session = Depends(get_session)
):
  headers:Query = session.query(Report.header)
  return headers

async def get_current_users_header_query(
  query:Query = Depends(get_header_query),
  current_user:User = Depends(get_current_user)
):
  headers = query.filter(
    Report.username==current_user.username
  )
  return headers

async def get_current_users_header_by_localreportid(
  localreportid:int,
  query:Query=Depends(get_current_users_reports)
):
  header:Report=query.filter(
    Report.localreportid==localreportid
    ).one()
  try:
    output = ReportHeaderout(**header.header.__dict__)
    return output
  except ValidationError as e:
    print(e)
    assert HTTP_400_BAD_REQUEST

async def update_header_by_headerid(
  headerid:int,
  header:ReportHeaderin=Depends(),
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  query:ReportHeader = session.query(ReportHeader).filter(
    ReportHeader.headerid==headerid
  ).one()

  query.type=header.type
  output = ReportHeaderout(
    **query.__dict__.copy()
  )
  session.commit()
  return output
  
