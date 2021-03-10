from sqlalchemy.sql.elements import or_
from db import get_session
from apps.report.models import Report, ReportContent, ReportContentGroup,ReportHeader
from apps.report.scheme import ContentGroupin, ContentGroupout, Contentupdate, ReportHeaderin, ReportHeaderout, Reportin,Reportupdate, Reportout,Contentin,Contentout
from apps.register.models import User
from auth import get_current_user

from fastapi import Depends,HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session, Query
from pydantic.error_wrappers import ValidationError
from starlette.status import HTTP_400_BAD_REQUEST

from copy import deepcopy


def _create_localid(session:Session,username,table:object,idcolumn,tableproperty:str)->int:
  try:
    q = session.query(table).filter(
      table.username==username).order_by(
        desc(idcolumn)
        ).first()
    localid:int= getattr(q,tableproperty) +1
    return localid    
  except:
    localid=1
    return localid    
# For report: POST Method-------------------------------------------------------
async def create_new_report(
  input:Reportin,
  current_user:User=Depends(get_current_user),
  session:Session=Depends(get_session)):
  try:
    localreportid=_create_localid(session,current_user.username,Report,Report.localreportid,"localreportid")
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
  try:
    localheaderid=_create_localid(session,current_user.username,ReportHeader,ReportHeader.localheaderid,"localheaderid")
    adds = ReportHeader(
      type=header.type,
      username=current_user.username,
      localheaderid=localheaderid)
    session.add(adds)
    try:
      session.commit()
      reportheader = ReportHeaderout(
        **session.query(ReportHeader).filter(
          ReportHeader.username==current_user.username
          ).order_by(desc(ReportHeader.headerid)).first().__dict__
      )
      return reportheader
    except:
      session.rollback()
      raise HTTPException(status_code=400,detail="couldn't enter data to DB. try again or check your input.")
  except:
    raise HTTPException(status_code=400)


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
    ).one()

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

async def update_content_by_localcontentid(
  localcontentid:int,
  updates:Contentupdate,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
):
  try:
    target=session.query(ReportContent).filter(
      ReportContent.username==current_user.username,
      ReportContent.localcontentid==localcontentid
    ).one()
    target.updates(updates)
    result=target.__dict__.copy()
    try:
      session.commit()
      return Contentout(**result)
    except:
      session.rollback()
      raise HTTPException(status_code=400)
  except:
    raise HTTPException(status_code=400)

async def delete_content_by_localcontentid(
  localcontentid:int,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)):
  try:
    deletes=session.query(ReportContent).filter(
      ReportContent.username==current_user.username,
      ReportContent.localcontentid==localcontentid
    ).one()
    session.delete(deletes)
    try:
      session.commit()
      return {"status":True,"localcontentid": localcontentid}
    except:
      raise HTTPException(status_code=400)
  except:
    raise HTTPException(status_code=400)


async def create_contentgroup(
  adds:ContentGroupin,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
  ):
  try:
    localgroupid=_create_localid(session,current_user.username,ReportContentGroup,ReportContentGroup.localgroupid,"localgroupid")
    contentslist=session.query(ReportContent).filter(
      ReportContent.username==current_user.username,
      ReportContent.localcontentid.in_(adds.localcontentids)
    ).all()
    try:
      group=[{
        "username": current_user.username,
        "localgroupid": localgroupid,
        "contentid": content.contentid,
        "order": i} for i,content in enumerate(contentslist)]

      session.execute(ReportContentGroup.__table__.insert(), group)
      try:
        session.commit()
        addedgroup = session.query(ReportContentGroup).filter(
          ReportContentGroup.username==current_user.username,
          ReportContentGroup.localgroupid==localgroupid
        ).all()
        result=ContentGroupout(
          localgroupid=localgroupid,
          contents=[contenttable.content for contenttable in addedgroup])
        return result
      except:
        session.rollback()
        raise HTTPException(status_code=400,detail="Could not enter data.")
    except:
      session.rollback()
      raise HTTPException(status_code=400,detail="SQL-ERROR")
  except:
    raise HTTPException(status_code=400)

async def get_contentgroup(
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)):
  try:
    query=session.query(ReportContentGroup).filter(
      ReportContentGroup.username==current_user.username
    ).all()
    return query
  except:
    raise HTTPException(status_code=400)

async def get_contentgroup_by_localgroupid(
  localgroupid:int,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
  ):
  try:
    group = session.query(ReportContentGroup).filter(
      ReportContentGroup.username==current_user.username,
      ReportContentGroup.localgroupid==localgroupid
    ).order_by(ReportContentGroup.order).all()
    if group==[]:
      raise HTTPException(status_code=400)

    return ContentGroupout(
      localgroupid=localgroupid,
      contents=[c.content for c in group])
  except:
    raise HTTPException(status_code=400)

async def update_contentgroup_by_localgroupid(
  localgroupid:int,
  localcontentids:ContentGroupin,
  session:Session=Depends(get_session),
  current_user:User=Depends(get_current_user)
  ):
  oldlist=session.query(ReportContentGroup.localgroupid).filter(
    ReportContentGroup.username==current_user.username,
    ReportContentGroup.localgroupid==localgroupid
  ).all()
  groupid_to_delete=list(set(oldlist)-set(localcontentids.localcontentids))
  #delete content not in update contents.
  



    