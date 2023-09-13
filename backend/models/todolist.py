from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, case
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.base import BaseModel
from models.user import User
from models.student import Student
from models.subject import Subject


class Todolist(BaseModel):
    __tablename__ = "todolist"

    subject_id = Column(Integer, ForeignKey("subject.id"))
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    name = Column(String)
    time = Column(String)
    level = Column(String)
    status = Column(Boolean, default=False)

    subject = relationship("Subject", back_populates="todolist")
    student = relationship("Student", back_populates="todolist")
    teacher = relationship("Teacher", back_populates="todolist")

    @classmethod
    def get_list(cls):
        db = cls.db()
        data = db.query(
            func.json_build_object(
                'id', Student.id,
                'user_id', User.id,
                'fullname', func.concat(User.first_name, ' ', User.last_name)
            ).label('student'),
            func.json_build_object(
                'id', Subject.id,
                'name', Subject.name
            ).label('subject'),
            func.array_agg(
                func.json_build_object( 
                    'id', cls.id,
                    'name', cls.name,
                    'level', cls.level,
                    'time', cls.time,
                    'status', cls.status,
                )
            ).label('task')
        ).join(
            Student, Student.id == cls.student_id 
        ).join(
            User, Student.user_id == User.id
        ).join(
            Subject, Subject.id == cls.subject_id 
        ).filter(
            cls.active == 'true'
        ).group_by(
            Subject.id, Student.id, User.first_name, User.last_name, User.id
        ).all()

        datas = list(map(lambda x: {
            'student': x.student,
            'subject': x.subject,
            'task': x.task
        }, data))
        return datas
    
    @classmethod
    def get_id(cls, id: int):
        db = cls.db()
        # is_status = case((cls.status == True, 'Done'), else_= 'No Done')
        data = db.query(
            func.json_build_object(
                'id', Student.id,
                'user_id', User.id,
                'fullname', func.concat(User.first_name, ' ', User.last_name)
            ).label('student'),
            func.json_build_object(
                'id', Subject.id,
                'name', Subject.name
            ).label('subject'),
            func.array_agg(
                func.json_build_object( 
                    'id', cls.id,
                    'name', cls.name,
                    'level', cls.level,
                    'time', cls.time,
                    'status', cls.status,
                )
            ).label('task')
        ).join(
            Student, Student.id == cls.student_id 
        ).join(
            User, Student.user_id == User.id
        ).join(
            Subject, Subject.id == cls.subject_id 
        ).filter(
            User.id == id
        ).group_by(
            Subject.id, Student.id, User.first_name, User.last_name, User.id
        ).all()

        datas = list(map(lambda x: {
            'subject': x.subject,
            'task': x.task
        }, data))
        return datas