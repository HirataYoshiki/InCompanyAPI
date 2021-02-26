from pydantic import BaseModel
from typing import List,Optional



class Character_in(BaseModel):
  department:str
  position:str
  skills:Optional[List[str]]

class Character_out(BaseModel):
  id:int
  username:str
  department:str
  position:str
  skills:Optional[List]

class Character_update(BaseModel):
  department:str=""
  position:str=""
  skills:Optional[List[str]]