from fastapi import APIRouter
from schemas.subject import SubjectCreate, SubjectUpdate
from models.subject import Subject

router = APIRouter()


@router.get('/')
def read_subjects():
    subjects = Subject.get_list()
    return subjects

@router.get('/subject_of_user/{id}')
def read_subject(id: int):
    subject = Subject.get_id(id=id)
    return subject

@router.post("/")
def create_subject(create: SubjectCreate):
    new_subject = Subject.create(create=create)
    return new_subject


@router.delete('/{id}')
def delete_subject(id: int):
    subject_model = Subject()
    deleted_subject = subject_model.delete(id=id)
    return deleted_subject


@router.put('/{id}')
def update_subject(id: int, update: SubjectUpdate):
    update_subject = Subject.update(id=id, update=update)
    return update_subject
