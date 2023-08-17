from sqlalchemy import Column, Integer, ForeignKey, String, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, text, alias
from models.base import BaseModel
from models.teacher import Teacher
from models.user import User
from models.student import Student

user_alias = alias(User.__table__)


class Subject(BaseModel):
    __tablename__ = "subject"

    name = Column(String)
    class_room = Column(String)
    timetable = Column(String)

    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    student_ids = Column(ARRAY(Integer))
    teacher = relationship("Teacher", back_populates="subject")
    student = relationship("Student", back_populates="subject")
    attendance = relationship("Attendance", back_populates="subject")
  
    @classmethod
    def get_list(cls): 
        db = cls.db()  
        data = db.query(
            cls.id.label('id'),
            cls.name.label('name'),
            cls.class_room.label('class_room'),
            cls.timetable.label('timetable'),
            cls.active.label('active'),
            func.json_build_object(
                'teacher_id', Teacher.id,
                'fullname', func.concat(User.first_name, ' ', User.last_name)
            ).label('teacher'),
            func.array_agg(
                func.json_build_object( 
                    'student_id', Student.id,
                    'fullname', func.concat(user_alias.c.first_name, ' ', user_alias.c.last_name)
                )
            ).label('student')
            ).join(Teacher, cls.teacher_id == Teacher.id
            ).join(Student, text(f'{cls.student_ids} @> ARRAY[student.id]')
            ).join(User, Teacher.user_id == User.id
            ).join(user_alias, Student.user_id == user_alias.c.id
            ).group_by(cls.id, Teacher.id, User.first_name, User.last_name
            ).filter(cls.active == 'true').all()

        datas = list(map(lambda x: {
            'id': x.id,
            'name': x.name,
            'class_room': x.class_room,
            'timetable': x.timetable,
            'teacher': x.teacher,
            'student': x.student,   
            'active': x.active
        }, data))
        return datas

    @classmethod
    def get_id(cls, id: int):
        db = cls.db()
        user_info = db.query(
            User.id.label('user_id'),
            cls.id.label('id'),
            func.concat(User.first_name, ' ', User.last_name).label('fullname'),
            func.ARRAY_TO_STRING(func.ARRAY_AGG(cls.name), ', ').label('subject'),
            Teacher.id.label('teacher_id'),
            Student.id.label('student_id')
        ).outerjoin(Teacher, Teacher.user_id == User.id
        ).outerjoin(Student, Student.user_id == User.id
        ).join(cls, text(f'COALESCE(Teacher.id, Student.id) = ANY(subject.student_ids)')
        ).group_by(User.id, User.first_name, User.last_name, cls.id, Teacher.id, Student.id
        ).filter(
            User.id == id
        ).all()

        result_dict = {}
        for row in user_info:
            user_id = row.user_id
            if row.teacher_id:
                user_type = 'teacher'
                user_id = row.teacher_id
            elif row.student_id:
                user_type = 'student'
                user_id = row.student_id

            key = (user_id, row.fullname)
            if key not in result_dict:
                result_dict[key] = {
                    user_type: {f'{user_type}_id': user_id, 'fullname': row.fullname},
                    'subject': []
                }
            result_dict[key]['subject'].append({'subject_id': row.id, 'name': row.subject})

        result_list = list(result_dict.values())
        return result_list