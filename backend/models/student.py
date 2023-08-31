from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel



class Student(BaseModel):
    __tablename__ = "student"

    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    user = relationship("User", back_populates="student")
    subject = relationship("Subject", back_populates="student")
    attendance = relationship("Attendance", back_populates="student")
    todolist = relationship("Todolist", back_populates="student")

    @classmethod
    def get_list(cls):
        data = super().get_list()
        datas = list(map(lambda x: {
            'id': x.id,
            'user_id': x.user_id,
            'username': x.user.username,
            'first_name': x.user.first_name,
            'last_name': x.user.last_name,
            'role': x.user.role,
            'active': x.active
        }, data))
        return datas

    @classmethod
    def create_student(cls, user_id: int):
        db = cls.db()
        student = Student(user_id=user_id)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    @classmethod
    def update(cls, id: int):
        db = cls.db()
        student = db.query(cls).filter(cls.id == id).first()
        db.commit()
        db.refresh(student)
        return student
