from apps.register.models import User
from typing import Optional,List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session,Query

from auth import get_current_user
from db import get_session
from apps.report import scheme, models
from apps.report.control import *
from apps.register.control import get_editor_user
from apps.register.scheme import User_out

router= APIRouter(prefix='/reportapp')

class Reports:
  @router.get('/reports/all')
  async def editor_get_all_reports(
    editor:User=Depends(get_editor_user),
    session:Session=Depends(get_session)):
    try:
      query = session.query(models.Report).all()
      return query
    except:
      raise HTTPException(status_code=400)
  @router.get('/reports/{localreportid}',response_model=scheme.Reportout)
  async def editor_get_report(
    report: scheme.Reportout = Depends(get_current_users_reports_by_localreportid)):
    try:
      return report
    except:
      raise HTTPException(status_code=400)

  @router.post('/reports',response_model=scheme.Reportout)
  async def create_my_new_report(
    report:scheme.Reportout=Depends(create_new_report)):
    try:
      return report
    except:
      raise HTTPException(status_code=400)

  @router.get('/reports')
  async def get_my_reports(
    query:Query=Depends(get_current_users_reports)
    ):
    try:
      return query.all()
    except:
      raise HTTPException(status_code=400)

  @router.get('/reports/{localreportid}',response_model=scheme.Reportout)
  async def get_my_report_selected_by_id(
    report: scheme.Reportout = Depends(get_current_users_reports_by_localreportid)):
    try:
      return report
    except:
      raise HTTPException(status_code=400)

  @router.put('/reports/{localreportid}',response_model=scheme.Reportout)
  async def update_report(
    report:scheme.Reportout=Depends(update_current_users_reports_by_id)
  ):
    try:
      return report
    except:
      raise HTTPException(status_code=400)
    

  @router.delete('/reports/{localreportid}')
  async def delete_my_report(
    localreportid:int,
    session:Session=Depends(get_session),
    current_user:User=Depends(get_current_user)
    ):
    try:
      query:models.Report = session.query(models.Report).filter(
      models.Report.username==current_user.username,
      models.Report.localreportid==localreportid).one()

      session.delete(query)
      session.commit()
      return {"status":True,"data":localreportid}
    except:
      raise HTTPException(status_code=400)


class Headers:
  @router.post('/headers',response_model=scheme.ReportHeaderout)
  async def create_new_my_header(
    header:scheme.ReportHeaderout=Depends(create_new_header)
  ):
    try:
      return header
    except:
      raise HTTPException(status_code=400)

  @router.get('/headers')
  async def get_my_headers(
    headers: Query = Depends(get_current_users_header_query)
  ):
    try:
      return headers.all()
    except:
      raise HTTPException(status_code=400)
  
  @router.get('/headers/{localheaderid}')
  async def get_header_by_id(
    header:ReportHeaderout=Depends(get_current_users_header_by_localheaderid)
    ):
    try:
      return header
    except:
      raise HTTPException(status_code=400)


  @router.put('/headers/{localheaderid}',response_model=ReportHeaderout)
  async def update_header(
    updated_header:ReportHeaderout=Depends(update_header_by_localheaderid)
  ):
    try:
      return updated_header
    except:
      raise HTTPException(status_code=400)

  @router.delete('/headers/{localheaderid}')
  async def delete_header(
    result:dict=Depends(delete_header_by_id)
  ):
    try:
      return result
    except:
      return HTTPException(status_code=400)


class Content:
  @router.post('/contents',response_model=Contentout)
  async def create_new_content(
    content:Contentout=Depends(create_content)
  ):
    try:
      return content
    except:
      raise HTTPException(status_code=400)

  @router.get('/contents')
  async def get_content(
    contentlist:list=Depends(get_content_list)
  ):
    try:
      return contentlist
    except:
      raise HTTPException(status_code=400)

  @router.get('/contents/{localcontentid}',response_model=Contentout)
  async def get_content_by_id(
    content:Contentout=Depends(get_content_by_localcontentid)
  ):
    try:
      return content
    except:
      raise HTTPException(status_code=400)

  @router.put('/contents/{localcontentid}',response_model=Contentout)
  async def update_content(
    content:Contentout=Depends(update_content_by_localcontentid)
  ):
    try:
      return content
    except:
      raise HTTPException(status_code=400)

  @router.delete('/contents/{localcontentid}')
  async def delete_content(
    localcontentid:int,
    deletes=Depends(delete_content_by_localcontentid)
  ):
    try:
      return deletes
    except:
      raise HTTPException(status_code=400)


class Contentgroup:
  @router.post('/groups',response_model=ContentGroupout)
  async def create_report_group(
    contentgroup:ContentGroupout=Depends(create_contentgroup)
  ):
    try:
      return contentgroup
    except:
      raise HTTPException(status_code=400)

  @router.get('/groups')
  async def get_groups(
    groups=Depends(get_contentgroup)
    ):
    try:
      return groups
    except:
      raise HTTPException(status_code=400)
  
  @router.get('/groups/{localgroupid}',response_model=ContentGroupout)
  async def get_group_by_id(
    group=Depends(get_contentgroup_by_localgroupid)
  ):
    try:
      return group
    except:
      raise HTTPException(status_code=400)

  @router.put('/groups/{localgroupid}',response_model=ContentGroupout)
  async def update_group(
  group:ContentGroupout=Depends(update_contentgroup_by_localgroupid)
  ):
    try:
      return group
    except:
      raise HTTPException(status_code=400)
  @router.delete('/groups/{localgroupid}')
  async def delete_group(
    result=Depends(delete_contentgroup_by_localgroupid)
    ):
    try:
      return result
    except:
      raise HTTPException(status_code=400)
