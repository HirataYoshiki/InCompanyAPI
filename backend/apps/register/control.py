import fastapi
from auth import get_current_user
from apps.register.models import User

from fastapi import Depends,HTTPException

async def get_editor_user(current_user: User = Depends(get_current_user)):
  if current_user.editor:
    return current_user
  else:
    raise HTTPException(status_code=400, detail="Inactive user")

def test_editor_user(current_user: User=Depends(get_current_user)):
  def wrap(func):
    def wwrap(*args,**kwargs):
      if current_user.editor:
        func(*args,**kwargs)
      else:
        raise HTTPException(status_code=400, detail="Inactive user")
    return wwrap
  return wrap
