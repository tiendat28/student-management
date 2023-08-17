from pydantic import BaseModel

class TeacherBase(BaseModel):
    user_id: int

class TeacherCreate(TeacherBase):
    pass
class TeacherUpdate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    active: bool

    class Config:
        orm_mode = True