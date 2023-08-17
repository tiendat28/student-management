from fastapi import APIRouter
from schemas.answer import AnswerCreate, AnswerUpdate
from models.answer import Answer
from typing import List
router = APIRouter()


@router.get('/')
def read_answers():
    answers = Answer.get_list()
    return answers


@router.post("/")
def create_answer(create: List[AnswerCreate]):
    new_answer = Answer.create(create=create)
    return new_answer


@router.delete('/{id}')
def delete_answer(id: int):
    answer_model = Answer()
    deleted_answer = answer_model.delete(id=id)
    return deleted_answer


@router.put('/{id}')
def update_answer(id: int, update: AnswerUpdate):
    update_answer = Answer.update(id=id, update=update)
    return update_answer
