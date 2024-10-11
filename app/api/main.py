from fastapi import APIRouter
from app.api.routes import home, login, users

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(home.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
