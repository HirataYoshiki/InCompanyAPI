from db import get_session
from apps.report.models import Report
from apps.report.scheme import Reportin,Reportupdate
from apps.register.models import User
from auth import get_current_user

from fastapi import Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session,Query

from typing import Optional
import inspect


# For POST Method-------------------------------------------------------
async def create_new_report(
  title:str,teamid:Optional[int]=None,
  headerid:Optional[int]=None,
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)):
  dicts = _precreate_new_report(title,teamid,headerid)
  dicts["username"]=current_user.username

  q = session.query(Report).filter(Report.username==current_user.username).order_by(desc(Report.reportid)).first()
  try:
    localreportid= q.localreportid +1
  except:
    #for the first post
    localreportid=1
  dicts["localreportid"]=localreportid
  adds = Report(**dicts)
  session.add(adds)
  try:
    session.commit()
    return {"status":True,"data":adds}
  except Exception as e:
    print(e)
    session.rollback()
    return {"status":False}



def _precreate_new_report(title:str,teamid:Optional[int]=None,headerid:Optional[int]=None):
  dicts = get_args_of_current_function()
  validated_dict = _validate_report_in(dicts)
  return dicts


def _validate_report_in(dicts):
  try:
    reportin=Reportin(**dict)
    return dicts
  except:
    return False


def get_args_of_current_function():
  current_frame = inspect.currentframe()
  parent_frame = current_frame.f_back
  info = inspect.getargvalues(parent_frame)
  return {key: info.locals[key] for key in info.args}
#--------------------------------------------------------------------------------------

async def get_current_users_reports(current_user:User=Depends(get_current_user),session:Session=Depends(get_session)):
  query = session.query(Report).filter(Report.username==current_user.username)
  return query




