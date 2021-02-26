from fastapi import APIRouter,Depends
from sqlalchemy.orm.exc import MultipleResultsFound

from auth import get_current_user
from db import get_session
from . import scheme,models

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
    query = session.query(models.User).filter(models.User.username==user.username).one()
    session.commit()
  except MultipleResultsFound as milti:
    session.rollback()
    print(milti)
  except Exception as e:
    session.rollback()
    print(e)

  return {
    "status":"true",
    "item":query
    }

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
    "status":"true",
    "item":userid
    }

@router.get('/users')
async def get_all_users():
  session=get_session()
  query=session.query(models.User).all()
  return {"item":query}

@router.get('/users/me')
async def get_users_me(current_user: scheme.User_out = Depends(get_current_user)):
    return current_user

@router.put('users/me')
async def update_users_me(update:scheme.User_update,current_user: scheme.User_out = Depends(get_current_user)):
  session = get_session()
  query = session.query(models.User).filter(models.User.userid==current_user.userid).one()
  print("query: \n",query)
  if update.username != None:
    query.username=update.username
  if update.mailaddress != None:
    query.mailaddress = update.mailaddress
  if update.password != None:
    query.password = hashlib.sha256(update.encode()).hexdigest()
    
  session.add(update)
  try:
    session.commit()
  except Exception as e:
    session.rollback()
    print(e)

  return {
    "status":"true",
    "item":update
    }

