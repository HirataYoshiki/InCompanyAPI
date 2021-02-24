from Routers import routers
from auth import auth
from db import get_session
from . import scheme

@routers.post('/users')
def add_user(user:scheme.User_in):
  session = get_session()


if __name__=="__main__":
  print(auth)