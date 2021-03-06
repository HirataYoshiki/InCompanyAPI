from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session


from auth import get_current_user
from db import get_session
from apps.character import scheme,models
from apps.register.scheme import User_out

router= APIRouter()

@router.post('/characters',response_model=scheme.Character_out)
async def register_new_user(
  characters:scheme.Character_in,
  current_user:User_out=Depends(get_current_user),
  session:Session=Depends(get_session)
  ):
  try:
    try:
      strskills = ','.join(characters.skills)
    except:
      strskills=characters.skills
    NewUser = models.Character(
      username = current_user.username,
      department = characters.department,
      position = characters.position,
      skills=strskills
    )
    session.add(NewUser)
    session.commit()
    return scheme.Character_out(
      **session.query(models.Character).filter(models.Character.username==current_user.username).one().dictor()
      )
  except:
    raise HTTPException(status_code=400)

@router.get('/characters/me',response_model=scheme.Character_out)
async def get_my_character(
  current_user:User_out=Depends(get_current_user),
  session:Session=Depends(get_session)):
  
  try:
    query:models.Character = session.query(models.Character).filter(models.Character.username==current_user.username).one()
    res=scheme.Character_out(
      **query.dictor()
    )
    return res
  except:
    raise HTTPException(status_code=400,detail={"Error": "No header is registered."})
  
  
@router.put('/characters/me',response_model=scheme.Character_out)
async def update_my_character(
  characters:scheme.Character_update,
  current_user:User_out=Depends(get_current_user),
  session:Session=Depends(get_session)):
  query:models.Character=session.query(models.Character).filter(models.Character.username==current_user.username).one()
  query.updates(characters)
  d = query.dictor()
  try:
    session.commit()
    return scheme.Character_out(**d)
  except:
    session.rollback()
    raise HTTPException(status_code=400)

@router.delete('/characters/me')
async def delete_me(
  current_user:User_out=Depends(get_current_user),
  session:Session=Depends(get_session)):
  query = session.query(models.Character).filter(models.Character.username==current_user.username).one()
  session.delete(query)
  try:
    session.commit()
    return {"status":True,"data":query}
  except:
    session.rollback()
    raise HTTPException(status_code=400)