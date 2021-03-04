from pydantic import BaseModel
from typing import List,Optional

class User_in(BaseModel):
  username:str
  password:str
  editor:bool=False
  mailaddress:Optional[str]=None

class User_out(BaseModel):
  userid:int
  username:str
  password:str
  editor:bool
  mailaddress:Optional[str]=None

class User_update(BaseModel):
  username: Optional[str]=None
  mailaddress: Optional[str]=None
  password: Optional[str]=None