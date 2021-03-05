from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.elements import False_

from auth import get_current_user
from db import get_session
from apps.character import scheme,models
from apps.register.scheme import User_out

router= APIRouter()

@router.post('/characters')
async def register_new_user(
  characters:scheme.Character_in,
  current_user:User_out=Depends(get_current_user),
  session:Session=Depends(get_session)
  ):

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
    return {"status":False}
  return session.query(models.Character).filter(models.Character.username==current_user.username).one()

@router.get('/characters/me')
async def get_my_character(current_user:User_out=Depends(get_current_user)):
  session = get_session()
  try:
    query = session.query(models.Character).filter(models.Character.username==current_user.username).one()
    return {
      "status":True,
      "data":query
    }
  except NoResultFound as e:
    print(e)
    return {"status":False,"data":"Not Registered.try to post quest @ /characters/me with params... department:str,position:str,skills:str[...]"}

@router.put('/characters/me')
async def update_my_character(
  characters:scheme.Character_update,
  current_user:User_out=Depends(get_current_user)):
  session = get_session()
  query=session.query(models.Character).filter(models.Character.username==current_user.username).one()
  if characters.department:
    query.department=characters.department
  if characters.position:
    query.position=characters.position
  query.skills=characters.skills
  try:
    session.commit()
    return {
      "status":True,
      "data":session.query(models.Character).filter(models.Character.username==current_user.username).one()
    }
  except Exception as e:
    session.rollback()
    print(e)
    return {"status":False}

@router.delete('/characters/me')
async def delete_me(current_user:User_out=Depends(get_current_user)):
  session = get_session()
  query = session.query(models.Character).filter(models.Character.username==current_user.username).one()
  session.delete(query)
  try:
    session.commit()
    return {"status":True,"data":query}
  except Exception as e:
    session.rollback()
    print(e)
    return {"status":False}
  