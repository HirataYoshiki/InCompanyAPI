from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext


class Develop:
  user_name="my"
  password="my"
  host= "incompanyapi_db"
  database_name = "my"

  config = {
    "DB_URL": 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
),
    "DEBUG":True,
    "OAUTH2_SCHEME":OAuth2PasswordBearer(tokenUrl="token"),
    "PWD_CONTEXT":CryptContext(schemes=["bcrypt"], deprecated="auto"),
    "ALGORITHM":"HS256",
    "ACCESS_TOKEN_EXPIRE_MINUTES":30,
    "SECRET_KEY":"aaf69e6b336b5177561cf1b1f50b5c9577909e8702428d5d9ca4065d25290b30"
  }
class Test:
  user_name="my"
  password="my"
  host= "incompanyapi_db"
  database_name = "test"

  config = {
    "DB_URL": 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name)}

class Product:
  config = {
    "DB_URL":"",
    "DEBUG":False
  }