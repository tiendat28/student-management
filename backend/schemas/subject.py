from pydantic import BaseModel

class SubjectBase(BaseModel):
    name: str
    class_room : str
    timetable : str
    teacher_id: int
    student_ids: list[int]

class SubjectCreate(SubjectBase):
    pass
class SubjectUpdate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    active: bool
    class Config:
        orm_mode = True