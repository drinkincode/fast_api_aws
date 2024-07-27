from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Take a sip"}

@router.get("/page")
async def oauth_end():
    return {"message": "Page"}

@router.get("/page/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/page/{username}")
async def read_user(username: str):
    return {"username": username}