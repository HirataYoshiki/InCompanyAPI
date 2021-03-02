from apps.register.models import User
from typing import Optional,List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session,Query

from auth import get_current_user
from db import get_session
from apps.report import scheme,models
from apps.report.control import create_new_report,get_current_users_reports
from apps.register.control import get_editor_user
from apps.register.scheme import User_out

router= APIRouter()

@router.get('/reports/all')
async def get_all_reports(
  editor:User_out=Depends(get_editor_user),
  session:Session=Depends(get_session)):
  query = session.query(models.Report).all()
  return {"status":True,"data":query}

@router.post('/reports/me')
async def create_my_new_report(
  report:models.Report=Depends(create_new_report)):
  return report

@router.get('/reports/me')
async def get_my_reports(
  query:Query=Depends(get_current_users_reports)
  ):
  return {"status":True,"data":query.all()}

@router.get('/reports/me/{localreportid}')
async def get_my_report_selected_by_id(
  localreportid:int,
  query:Query=Depends(get_current_users_reports)):
  try:
    report = query.filter(models.Report.localreportid==localreportid).one()
    return {"status":True,"data":report}
  except Exception as e:
    print(e)
    return {"status":False}

@router.put('/reports/me/{localreportid}')
async def update_report(
  localreportid:int,
  update:scheme.Reportupdate,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  query:models.Report = session.query(models.Report).filter(
    models.Report.username==current_user.username,
    models.Report.localreportid==localreportid).one()

  query.updates(update)
  session.commit()

  return {
    "staus":True,
    "data": session.query(models.Report).filter(
    models.Report.username==current_user.username,
    models.Report.localreportid==localreportid).one()}





