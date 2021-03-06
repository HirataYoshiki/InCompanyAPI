from pydantic import BaseModel
from typing import Any, Optional,List
from datetime import datetime

class Reportin(BaseModel):
  title:str
  teamid:Optional[int]=None
  headerid:Optional[int]=None
  contentgroupid:Optional[int]=None

class Reportout(BaseModel):
  reportid:int
  localreportid:int
  username:str
  title:str
  contentsid:Optional[int]=None
  timestamp:Optional[datetime]=None
  teamid:Optional[int]=None
  headerid:Optional[int]=None

class Reportupdate(BaseModel):
  title:Optional[str]=None
  contentsid:Optional[int]=None
  teamid:Optional[int]=None
  headerid:Optional[int]=None

class ReportHeaderin(BaseModel):
  type:str

class ReportHeaderout(BaseModel):
  localheaderid:int
  type:str

class Contentin(BaseModel):
  content:str

class Contentout(BaseModel):
  localcontentid:int
  content:str
  groupid:Optional[int]=None

class Contentupdate(BaseModel):
  content:Optional[str]=None

class ContentGroupin(BaseModel):
  localcontentids:List[int]

class ContentGroupout(BaseModel):
  localgroupid:int
  contents:List[Any]