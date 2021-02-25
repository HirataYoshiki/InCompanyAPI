from fastapi import APIRouter
from auth import auth
from db import get_session
from . import scheme,models

routers= APIRouter()

@routers.post('/users')
async def add_user(user:scheme.User_in):
  session = get_session()
  adds=models.User(
    username=user.username,
    password = user.password,
    mailaddress = user.mailaddress
  )
  session.add(adds)
  try:
    session.commit()
  except:
    session.rollback()
    print("rollbaced")

  return {"status":"true"}

@routers.get('/users')
async def get_all_users():
  session=get_session()
  query=session.query(models.User).all()
  return {"item":query}

if __name__=="__main__":
  print(auth)