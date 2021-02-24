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
    "DEBUG":True
  }

class Product:
  config = {
    "DB_URL":"",
    "DEBUG":False
  }