from fastapi import APIRouter
from schemas.questions import QuestionCreate, QuestionUpdate
from models.questions import Question
router = APIRouter()


@router.get('/')
def read_questions():
    questions = Question.get_list()
    return questions


@router.post("/")
def create_question(create: QuestionCreate):
    new_question = Question.create(create=create)
    return new_question


@router.delete('/{id}')
def delete_question(id: int):
    question_model = Question()
    deleted_question = question_model.delete(id=id)
    return deleted_question


@router.put('/{id}')
def update_question(id: int, update: QuestionUpdate):
    update_question = Question.update(id=id, update=update)
    return update_question
