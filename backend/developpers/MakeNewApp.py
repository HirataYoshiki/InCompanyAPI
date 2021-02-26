from pathlib import Path
import os

backend = Path(__file__).parent.parent
apps = backend/'./apps'

def MakeNewApp(appname):
  newapp=apps/'./{}'.format(appname)
  print(newapp)
  if newapp.exists():
    print("exist")
    return False
  newapp.mkdir()
  return newapp

def MakeMSRfiles(newapp):
  files = {
    "model":{
      "dir":newapp/'./models.py',
      "text":"from sqlalchemy.sql.sqltypes import Boolean\nfrom db import Base,engine\nfrom sqlalchemy import Column, Integer, String, Boolean"
    },
    "scheme":{
      "dir":newapp/'./scheme.py',
      "text":"from pydantic import BaseModel\nfrom typing import List,Optional"
    },
    "router":{
      "dir":newapp/'./router.py',
      "text":"from typing import Optional\nfrom fastapi import APIRouter,Depends\n\nfrom auth import get_current_user\nfrom db import get_session\nfrom . import scheme,models\n\nrouter= APIRouter()"
    }
  }

  for _,file in files.items():
    with open(file["dir"],'w') as f:
      f.write(file["text"])

if __name__=="__main__":
  AppName=input("Input New App Name Here\n\t->")
  newapp=MakeNewApp("testapp")
  MakeMSRfiles(newapp)
