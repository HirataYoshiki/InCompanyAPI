from pydantic import BaseModel
from typing import List,Optional

class User_in(BaseModel):
  username:str
  password:str
  mailaddress:Optional[str]=None


class User_out(BaseModel):
  userid:int
  username:str
  password:str
  mailaddress:Optional[str]=None