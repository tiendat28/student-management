from fastapi import APIRouter
from models.token import Token
from models.user import User


router = APIRouter()

@router.post('/')
def login(username: str, password: str):
    user = User.auther_user(username=username, password=password)
    if user:
        token = Token.create_token(data={'id': user.id, 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name})
    return token

