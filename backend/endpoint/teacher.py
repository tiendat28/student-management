from fastapi import APIRouter
from schemas.user import UserCreate, UserUpdate
from models.user import User
from models.teacher import Teacher
from models.subject import Subject
from models.attendance import Attendance


router = APIRouter()


@router.get('/')
def read_teachers():
    teachers = Teacher.get_list()
    return teachers


@router.post("/")
def create_teacher(create: UserCreate):
    new_user = User.create(create=create)
    if new_user.role == 'Teacher':
        user_id = new_user.id
        new_teacher = Teacher.create_teacher(user_id=user_id)

    return {
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'user_id': new_user.id,
        'id': new_teacher.id
    }


@router.delete('/{id}')
def delete_teacher(id: int):
    teacher_model = Teacher()
    deleted_teacher = teacher_model.delete(id=id)
    return deleted_teacher


@router.put('/{id}')
def update_teacher(id: int, update: UserUpdate):
    teacher = Teacher.update(id=id)
    id = teacher.user_id
    update_teacher = User.update(id=id, update=update)
    return update_teacher
