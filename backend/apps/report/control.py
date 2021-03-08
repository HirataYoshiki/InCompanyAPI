from db import get_session
from apps.report.models import Report, ReportContent,ReportHeader
from apps.report.scheme import ReportHeaderin, ReportHeaderout, Reportin,Reportupdate, Reportout,Contentin,Contentout
from apps.register.models import User
from auth import get_current_user

from fastapi import Depends,HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session, Query
from pydantic.error_wrappers import ValidationError
from starlette.status import HTTP_400_BAD_REQUEST



# For report: POST Method-------------------------------------------------------
async def create_new_report(
  input:Reportin,
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)):
  try:
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
    
    session.commit()
    report = session.query(Report).filter(
      Report.username==current_user.username,
      Report.localreportid==localreportid
      ).one()
    return Reportout(**report.__dict__)
  except:
    session.rollback()
    raise HTTPException(status_code=400)


#--------------------------------------------------------------------------------------

async def get_current_users_reports(
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)
  ):
  try:
    query:Query = session.query(Report).filter(Report.username==current_user.username)
    return query
  except:
    raise HTTPException(status_code=400)

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
  update:Reportupdate,
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session) 
):
  try:
    report:Report = session.query(Report).filter(
      Report.username==current_user.username,
      Report.localreportid==localreportid
      ).one()
    
    updated:Report=report.updates(update)
    copy= updated.__dict__.copy()
    session.commit()
    print(copy)
    return Reportout(**copy)
  except:
    raise HTTPException(status_code=400)



async def create_new_header(
  header:ReportHeaderin,
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
    raise HTTPException(status_code=400)

async def update_header_by_headerid(
  headerid:int,
  header:ReportHeaderin,
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

async def delete_header_by_id(
  localheaderid:int,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  try:
    deletes=session.query(ReportHeader).filter(
      ReportHeader.username==current_user.username,
      ReportHeader.localheaderid==localheaderid
    ).one

    session.delete(deletes)
    return {"id": localheaderid}
  except:
    raise HTTPException(status_code=400)

async def create_report_content(
  content:Contentin,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  try:
    localcontentid=session.query(ReportContent).filter(
      ReportContent.username==current_user.username
    ).count()+1
    addcontent=ReportContent(
      **content.__dict__,
      localcontentid=localcontentid,
      username=current_user.username
    )
    session.add(addcontent)
    try:
      session.commit()
    except:
      session.rollback()
      raise HTTPException(status_code=400)
  except:
    raise HTTPException(status_code=400)

async def _get_report_content_query(
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)
):
  try:
    query:Query=session.query(ReportContent).filter(
    ReportContent.username==current_user.username
  )
    return query
  except:
    raise HTTPException(status_code=400) 

async def get_report_content_all(
  query:Query=Depends(_get_report_content_query)
):
  try:
    contentsall=query.all()
    return contentsall
  except:
    raise HTTPException(status_code=400)

async def get_report_content_by_localcontentid(
  localcontentid:int,
  query:Query=Depends(_get_report_content_query)
):
  try:
    content=query.filter(
      ReportContent.localcontentid==localcontentid
    ).one_or_none()
    if content==None:
      raise HTTPException(status_code=400)
    return content
  except:
    raise HTTPException(status_code=400)


async def create_content(
  content:Contentin,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  try:
    try:
      localcontentid:int = session.query(ReportContent).filter(
          ReportContent.username==current_user.username
          ).order_by(desc(ReportContent.localcontentid)
          ).first().localcontentid+1
    except:
      localcontentid=1
    adds=ReportContent(
      **content.__dict__,
      username=current_user.username,
      localcontentid=localcontentid
    )
    
    show=adds.__dict__.copy()
    session.add(adds)
    session.commit()
    return Contentout(**show)
  except:
    raise HTTPException(status_code=400)

async def _get_my_content_query(
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  try:
    query:Query=session.query(ReportContent).filter(
      ReportContent.username==current_user.username
    )
    return query
  except:
    raise HTTPException(status_code=400)

async def get_content_list(
  query:Query=Depends(_get_my_content_query)
):
  try:
    return query.all()
  except:
    raise HTTPException(status_code=400)

async def get_content_by_localcontentid(
  localcontentid:int,
  query:Query=Depends(_get_my_content_query)
):
  try:
    content=query.filter(ReportContent.localcontentid==localcontentid).one_or_none()
    return Contentout(**content.__dict__)
  except:
    raise HTTPException(status_code=400)
