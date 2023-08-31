from fastapi import APIRouter
from schemas.todolist import TodolistCreate, TodolistUpdate
from models.todolist import Todolist

router = APIRouter()


@router.get('/')
def read_todolist():
    todolist = Todolist.get_list()
    return todolist

@router.get('/{id}')
def read_todo(id: int):
    todolist = Todolist.get_id(id=id)
    return todolist

@router.post("/")
def create_todolist(create: TodolistCreate):
    new_todolist = Todolist.create(create=create)
    return new_todolist


@router.delete('/{id}')
def delete_todolist(id: int):
    todolist_model = Todolist()
    deleted_todolist = todolist_model.delete(id=id)
    return deleted_todolist


@router.put('/{id}')
def update_todolist(id: int, update: TodolistUpdate):
    update_todolist = Todolist.update(id=id, update=update)
    return update_todolist
