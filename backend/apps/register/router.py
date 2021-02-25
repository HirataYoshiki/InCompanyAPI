from fastapi import APIRouter
from auth import auth
from db import get_session
from . import scheme,models

import hashlib

routers= APIRouter()

@routers.post('/users')
async def add_user(user:scheme.User_in):
  session = get_session()
  hashedpassword = hashlib.sha256(user.password.encode()).hexdigest()
  adds=models.User(
    username=user.username,
    password = hashedpassword,
    mailaddress = user.mailaddress
  )
  session.add(adds)
  try:
    session.commit()
  except Exception as e:
    session.rollback()
    print(e)

  return {"status":"true"}

@routers.get('/users')
async def get_all_users():
  session=get_session()
  query=session.query(models.User).all()
  return {"item":query}

if __name__=="__main__":
  print(auth)