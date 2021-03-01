from db import get_session
from apps.report import models
from apps.report.scheme import Reportin
from auth import get_current_user
from apps.register.models import User

from fastapi import Depends
from sqlalchemy.orm import Session

from typing import Optional
import inspect



async def create_new_report(title:str,teamid:Optional[int]=None,headerid:Optional[int]=None,current_user:User=Depends(get_current_user)):
  dicts = precreate_new_report(title,teamid,headerid)
  dicts["username"]=current_user.username
  return models.Report(**dicts)

def precreate_new_report(title:str,teamid:Optional[int]=None,headerid:Optional[int]=None):
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


async def get_current_users_reports(current_user:User=Depends(get_current_user),session:Session=Depends(get_session)):
  query = session.query(models.Report).filter(models.Report.username==current_user.username)
  return query