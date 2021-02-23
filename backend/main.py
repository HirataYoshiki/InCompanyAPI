from fastapi import FastAPI
import uvicorn

import router

app = FastAPI()

app.include_router(router.routers)

if __name__ == "__main__":
  uvicorn.run(app)