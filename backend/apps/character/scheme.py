from pydantic import BaseModel
from typing import List,Optional



class Character_in(BaseModel):
  department:str
  position:str
  skills:Optional[List[str]]=None

class Character_out(BaseModel):
  id:int
  username:str
  department:str
  position:str
  skills:Optional[List]=None

class Character_update(BaseModel):
  department:Optional[str]=None
  position:Optional[str]=None
  skills:Optional[List[str]]=None