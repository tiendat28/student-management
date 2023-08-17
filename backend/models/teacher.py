from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

class Teacher(BaseModel):
    __tablename__ = "teacher"

    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    user = relationship("User", back_populates="teacher")
    subject = relationship("Subject", back_populates="teacher")
    attendance = relationship("Attendance", back_populates="teacher")

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
    def create_teacher(cls, user_id: int):
        db = cls.db()
        teacher = cls(user_id=user_id)
        db.add(teacher)
        db.commit()
        db.refresh(teacher)
        return teacher

    @classmethod
    def update(cls, id: int):
        db = cls.db()
        teacher = db.query(cls).filter(cls.id == id).first()
        db.commit()
        db.refresh(teacher)
        return teacher