from fastapi import APIRouter
from schemas.attendance import AttendanceCreate, AttendanceUpdate
from models.attendance import Attendance
from typing import List
router = APIRouter()


@router.get('/')
def read_attendances():
    attendances = Attendance.get_list()
    return attendances


@router.post("/")
def create_attendance(create: List[AttendanceCreate]):
    new_attendance = Attendance.create(create=create)
    return new_attendance


@router.delete('/{id}')
def delete_attendance(id: int):
    attendance_model = Attendance()
    deleted_attendance = attendance_model.delete(id=id)
    return deleted_attendance


@router.put('/{id}')
def update_attendance(id: int, update: AttendanceUpdate):
    update_attendance = Attendance.update(id=id, update=update)
    return update_attendance
