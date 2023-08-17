from pydantic import BaseModel
from datetime import datetime

class AttendanceBase(BaseModel): 
    subject_id: int
    teacher_id: int
    student_id: int
    date: datetime
    status: str
class AttendanceCreate(AttendanceBase):
    pass
class AttendanceUpdate(AttendanceBase):
    pass

class Attendance(AttendanceBase): 
    id: int
    active: bool
    class Config:
        orm_mode = True
