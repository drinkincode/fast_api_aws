from fastapi import FastAPI
import uvicorn
from routers import oauth
from routers import api

app = FastAPI()

app.include_router(oauth.router)
app.include_router(api.router)

uvicorn.run(app, port=80)