from apps.register.models import User
from typing import Optional

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

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
  try:
    session.commit()
    return {
      "status": True,
      "data": query
    } 
  except:
    session.rollback()
    return {"status": False}

@router.post('/reports')
async def create_my_new_report(
  report:models.Report=Depends(create_new_report),
  session:Session=Depends(get_session)):
  session.add(report)
  try:
    session.commit()
    db = get_current_users_reports()
    query=db.filter(models.Report.title==report.title).one()
    return {
      "status":True,
      "data":query
      }
  except Exception as e:
    print(e)
    return {"status":False}

@router.get('/reports')
async def get_my_reports(
  session:Session=Depends(get_current_users_reports)):
  return {"status":True,"data":session.all()}

