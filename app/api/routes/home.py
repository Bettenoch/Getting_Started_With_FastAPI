from fastapi import APIRouter


router = APIRouter()

@router.get('/')

def get_home_page():
    return {'message': 'Welcome to the FastAPI application!'}