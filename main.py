from fastapi import FastAPI
import uvicorn
from app.routers import oauth
from app.routers import api

app = FastAPI()

app.include_router(oauth.router)
app.include_router(api.router)

uvicorn.run(app, port=80)