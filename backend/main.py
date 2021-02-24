from fastapi import FastAPI
import uvicorn

import Routers


app = FastAPI()
app.include_router(
  Routers.routers
  )

@app.get('/')
def hello():
  return {"text":"hello"}
  

if __name__ == "__main__":
  uvicorn.run(app,port=8000)