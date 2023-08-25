from sqlalchemy import Column, Integer, ForeignKey, DATE,String, select
from sqlalchemy.orm import relationship, aliased
from sqlalchemy.sql import func
from models.subject import Subject
from models.student import Student
from models.user import User
from models.base import BaseModel

class Attendance(BaseModel):
    __tablename__ = "attendance"

    subject_id = Column(Integer, ForeignKey("subject.id"))
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    date = Column(DATE)
    status = Column(String)

    teacher = relationship("Teacher", back_populates="attendance")
    student = relationship("Student", back_populates="attendance")
    subject = relationship("Subject", back_populates="attendance")


    @classmethod
    def get_list(cls):
        data = super().get_list()
        result = {}

        for item in data:
            subject_id = item.subject_id
            date = item.date
            student_id = item.student_id
            status = item.status

            if subject_id not in result:
                result[subject_id] = {"date": []}

            date_found = False
            for d in result[subject_id]["date"]:
                if d["date"] == date:
                    date_found = True
                    d["student"].append({"student_id": student_id, "status": status})
                    break

            if not date_found:
                result[subject_id]["date"].append({"date": date, "student": [{"student_id": student_id, "status": status}]})

        final_result = [{"subject_id": key, "date": value["date"]} for key, value in result.items()]

        return final_result
        

    @classmethod
    def create(cls, create:list):
        db = cls.db()
        objects = []
        for user in create:
            db_item = cls(**user.dict())
            objects.append(db_item)
        db.bulk_save_objects(objects)
        db.commit()
        return objects
  