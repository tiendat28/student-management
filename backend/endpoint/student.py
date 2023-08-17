from fastapi import APIRouter
from schemas.user import UserCreate, UserUpdate
from models.user import User
from models.student import Student


router = APIRouter()

@router.get('/')
def read_students():
    students = Student.get_list()
    return students


@router.post("/")
def create_student(create: UserCreate):
    new_user = User.create(create=create)
    if new_user.role == 'Student':
        user_id = new_user.id
        new_student = Student.create_student(user_id=user_id)

    return {
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'user_id': new_user.id,
        'id': new_student.id
    }


@router.delete('/{id}')
def delete_student(id: int):
    student_model = Student()
    delete_student = student_model.delete(id=id)
    return delete_student


@router.put('/{id}')
def update_student(id: int, update: UserUpdate, ):
    student = Student.update(id=id)
    id = student.user_id
    update_student = User.update(id=id, update=update)
    return update_student
