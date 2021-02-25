from fastapi import FastAPI
import uvicorn

import Routers
from apps.register.router import routers as registerrouter
from auth import router as authrouter


app = FastAPI()
app.include_router(Routers.routers)
app.include_router(registerrouter)
app.include_router(authrouter)

@app.get('/')
def hello():
  return {"text":"hello"}
  

if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=8080)