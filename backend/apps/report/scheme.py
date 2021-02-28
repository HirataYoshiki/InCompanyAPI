from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Reportin(BaseModel):
  username:str
  title:str
  teamid:Optional[int]=None
  headerid:Optional[int]=None

class Reportout(BaseModel):
  reportid:int
  username:str
  title:str
  contentsid:int
  timestamp:datetime
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

