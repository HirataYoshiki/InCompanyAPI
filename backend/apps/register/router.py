from fastapi import APIRouter,Depends
from sqlalchemy.orm.exc import MultipleResultsFound

from auth import get_current_user
from db import get_session
from apps.register import scheme,models
from apps.register.control import get_editor_user

import hashlib

router= APIRouter()

@router.post('/users')
async def add_user(user:scheme.User_in):
  session = get_session()
  hashedpassword = hashlib.sha256(user.password.encode()).hexdigest()
  adds=models.User(
    username=user.username,
    password = hashedpassword,
    mailaddress = user.mailaddress,
    editor=user.editor
  )
  try:
    session.add(adds)
    session.commit()
    query = session.query(models.User).filter(models.User.username==user.username).one()
    return {
      "status":True,
      "item":query
    }
  except MultipleResultsFound as milti:
    session.rollback()
    print(milti)
    return {"status":False,"text":"The user already exists"}
  except Exception as e:
    session.rollback()
    print(e)
    return {"status":False}

  

@router.delete('/users/{userid}')
async def delete_user(userid:int):
  session = get_session()
  deletes = session.query(models.User).filter(models.User.userid==userid).one()
  session.delete(deletes)
  try:
    session.commit()
  except Exception as e:
    session.rollback()
    print(e)

  return {
    "status":True,
    "item":userid
    }

@router.get('/users')
async def get_all_users(editor:models.User=Depends(get_editor_user)):
  session=get_session()
  query=session.query(models.User).all()
  return {"item":query}

@router.get('/users/me')
async def get_users_me(current_user: scheme.User_out = Depends(get_current_user)):
    return current_user

@router.put('/users/me')
async def update_users_me(
  update:scheme.User_update,
  current_user: scheme.User_out = Depends(get_current_user)):
  session = get_session()
  query = session.query(models.User).filter(models.User.userid==current_user.userid).one()
  if update.username:
    query.username=update.username
  if update.mailaddress:
    query.mailaddress = update.mailaddress
  if update.password:
    query.password = hashlib.sha256(update.password.encode()).hexdigest()
    
  session.add(query)
  try:
    session.commit()
    return {
      "status":True,
      "item":session.query(models.User).filter(models.User.userid==current_user.userid).one()
      }
  except Exception as e:
    session.rollback()
    print(e)

  

