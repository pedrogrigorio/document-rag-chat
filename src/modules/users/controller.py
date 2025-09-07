from fastapi import APIRouter

from .model import UserModel

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def create_user() -> object:
    hashed_pw = "teste"
    user = UserModel(email="teste@gmail.com", password_hash=hashed_pw)
    print("old", user)
    await user.insert()
    print("new", user)
    return {"message": user}
