from apps.register.models import User
from typing import Optional,List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session,Query

from auth import get_current_user
from db import get_session
from apps.report import scheme, models
from apps.report.control import *
from apps.register.control import get_editor_user
from apps.register.scheme import User_out

router= APIRouter()

class Reports:
  @router.get('/reports/all')
  async def editor_get_all_reports(
    editor:User=Depends(get_editor_user),
    session:Session=Depends(get_session)):
    query = session.query(models.Report).all()
    return query

  @router.get('/reports/{reportid}',response_model=scheme.Reportout)
  async def editor_get_report(
    report: scheme.Reportout = Depends(get_current_users_reports_by_id)):
    return report

  @router.post('/reports',response_model=scheme.Reportout)
  async def create_my_new_report(
    report:scheme.Reportout=Depends(create_new_report)):
    return report

  @router.get('/reports')
  async def get_my_reports(
    query:Query=Depends(get_current_users_reports)
    ):
    try:
      return query.all()
    except:
      print("Error: router.py")

  @router.get('/reports/{localreportid}',response_model=scheme.Reportout)
  async def get_my_report_selected_by_id(
    report: scheme.Reportout = Depends(get_current_users_reports_by_id)):
    return report

  @router.put('/reports/{localreportid}',response_model=scheme.Reportout)
  async def update_report(
    report:scheme.Reportout=Depends(update_current_users_reports_by_id)
  ):
    return report
    

  @router.delete('/reports/{localreportid}')
  async def delete_my_report(
    localreportid:int,
    session:Session=Depends(get_session),
    current_user:User=Depends(get_current_user)
  ):
    query:models.Report = session.query(models.Report).filter(
      models.Report.username==current_user.username,
      models.Report.localreportid==localreportid).one()

    session.delete(query)
    session.commit()
    return {"status":True,"data":localreportid}

class Headers:
  @router.post('/reports/headers',response_model=scheme.ReportHeaderout)
  async def create_new_my_header(
    header:scheme.ReportHeaderout=Depends(create_new_header)
  ):
    return header

  @router.get('/reports/headers')
  async def get_my_headers(
    headers: Query = Depends(get_current_users_header_query)
  ):
    return headers.all()

  @router.get('/reports/{localreportid}/headers',response_model=scheme.ReportHeaderout)
  async def get_header_by_localreportid(
    header:scheme.ReportHeaderout=Depends(get_current_users_header_by_localreportid)
  ):
    return header

  @router.put('/reports/headers/{headerid}',response_model=ReportHeaderout)
  async def update_header(
    updated_header:ReportHeaderout=Depends(update_header_by_headerid)
  ):
    return updated_header



