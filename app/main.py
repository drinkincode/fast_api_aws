from fastapi import FastAPI
import uvicorn
from routers import oauth
from routers import api

app = FastAPI()

app.include_router(oauth.router)
app.include_router(api.router)

# uvicorn.run(app)
# uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")