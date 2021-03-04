from fastapi import FastAPI
import uvicorn
from Routers import ROUTERS
from db import engine


app = FastAPI()

for router in ROUTERS:
  app.include_router(router)

@app.get('/')
def hello():
  return {"text":"hello"}
  
@app.on_event("startup")
async def startup():
  engine.connect()

@app.on_event("shutdown")
async def shutdown():
  engine.disconnect()

if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=8080)