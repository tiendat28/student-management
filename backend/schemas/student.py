from pydantic import BaseModel

class StudentBase(BaseModel): 
    user_id: int
class StudentCreate(StudentBase):
    pass
class StudentUpdate(StudentBase):
    pass

class Student(StudentBase): 
    id: int
    active: bool
    class Config:
        orm_mode = True
