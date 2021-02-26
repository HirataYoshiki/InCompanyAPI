from pydantic import BaseModel
from typing import List,Optional

class User_in(BaseModel):
  username:str
  password:str
  mailaddress:Optional[str]=None
  editor:bool=False

class User_out(BaseModel):
  userid:int
  username:str
  hashedpassword:str
  mailaddress:Optional[str]=None
  editor:bool

class User_update(BaseModel):
  username: Optional[str]=None
  mailaddress: Optional[str]=None
  password: Optional[str]=None