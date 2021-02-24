from pydantic import BaseModel
from typing import List,Optional
import hashlib

class User_in(BaseModel):
  username:str
  password:str
  mailaddress:Optional[str]=None

  @property
  def hassedpassword(self):
    return hashlib.sha256(self.password.encode()).hexdigest()

class User_out(BaseModel):
  userid:int
  username:str
  mailaddress:Optional[str]=None