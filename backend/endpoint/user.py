from fastapi import APIRouter
from models.user import User
from schemas.user import UserCreate
router = APIRouter()


@router.get('/')
def read_users():
    users = User.get_list()
    return users

@router.get('/{id}')
def read_users(id: int):
    users = User.get_one(id=id)
    return users

@router.post("/")
def create_user(create: UserCreate):
    new_user = User.create(create=create)
    return {
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'role': new_user.role
    }

@router.delete('/{id}')
def delete_user(id: int):
    user_model = User()
    deleted_user = user_model.delete(id=id)
    return deleted_user