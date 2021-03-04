from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Reportin(BaseModel):
  title:str
  teamid:Optional[int]=None
  headerid:Optional[int]=None

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
  headerid:int
  type:str


class Contentin(BaseModel):
  contentsid:int
  content:str

class Contentout(BaseModel):
  contentid:int
  contentsid:int
  content:str

