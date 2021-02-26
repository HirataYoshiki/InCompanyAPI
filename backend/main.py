from fastapi import FastAPI
import uvicorn
from Routers import ROUTERS


app = FastAPI()

for router in ROUTERS:
  app.include_router(router)

@app.get('/')
def hello():
  return {"text":"hello"}
  

if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=8080)