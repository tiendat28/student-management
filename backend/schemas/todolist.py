from pydantic import BaseModel

class TodolistBase(BaseModel):
    subject_id: int = None
    teacher_id: int = None
    student_id: int = None
    name: str
    time: str
    level: str
    status: bool
class TodolistCreate(TodolistBase):
    pass
class TodolistUpdate(TodolistBase):
    pass

class Todolist(TodolistBase):
    id: int
    active: bool
    class Config:
        orm_mode = True