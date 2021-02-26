from fastapi import APIRouter,Depends

from auth import get_current_user
from db import get_session
from apps.character import scheme,models
from apps.register.scheme import User_out


router= APIRouter()

@router.post('/characters')
async def register_new_user(
  characters:scheme.Character_in,
  current_user:User_out=Depends(get_current_user)
  ):

  session = get_session()
  NewUser = models.Character(
    username = current_user.username,
    department = characters.department,
    position = characters.position,
    skills=characters.skills
  )
  session.add(NewUser)
  try:
    session.commit()
  except Exception as e:
    session.rollback()
    print(e)
    return {"status":"Error"}
  return {
    "status":"OK",
    "username":current_user.username,
    "characters":characters
    } 

@router.get('/characters/me')
async def get_my_character(current_user:User_out=Depends(get_current_user)):
  session = get_session()
  query = session.query(models.Character).filter(models.Character.username==current_user.username).one()
  return {
    "status":"OK",
    "data":query
  }