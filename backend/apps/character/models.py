from sqlalchemy.util.langhelpers import attrsetter
from db import Base,engine
from sqlalchemy import Column, String, Integer
from apps.character.scheme import Character_update

class Character(Base):
  __tablename__ = "character"
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50))
  department = Column(String(50))
  position = Column(String(50))
  # skills would be List -> String when insert
  skills = Column(String(300))

  def updates(self,update:Character_update):
    for k in self.__dict__.keys():
      for kk,vv in update.__dict__.items():
        if k==kk and vv is not None:
          setattr(self,k,vv)

  def dictor(self):
    d = {
      'id': self.id,
      'username': self.username,
      'department': self.department,
      'position': self.position,
      }
    if self.skills==None:
      skill = None
      d['skills']=skill
      return d
    else:
      try:
        skill = self.skills.split(",")
        d['skills']=skill
        return d
      except:
        skill = [self.skills]
        d['skills']=skill
        return d
    
    




if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)