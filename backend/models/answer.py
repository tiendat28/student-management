from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, case
from sqlalchemy.orm import relationship
from models.base import BaseModel
from sqlalchemy.sql import func
from models.user import User
from models.questions import Question

class Answer(BaseModel):
    __tablename__ = "answers"

    q_id = Column(Integer, ForeignKey("questions.id"))
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    select_answer = Column(String)
    is_correct = Column(Boolean)

    questions = relationship("Question", back_populates="answers")
    user = relationship("User", back_populates="answers")

    @classmethod
    def get_list(cls): 
        db = cls.db()  
        is_correct = case((cls.select_answer == Question.correct_answer, True), else_=False)
        correct_count = func.sum(func.cast(is_correct, Integer))
        data = db.query(
            cls.active.label('active'),
            func.json_build_object(
                'id', User.id,
                'fullname', func.concat(User.first_name, ' ', User.last_name),
                'score_total', correct_count
            ).label('user'),
            func.array_agg(
                func.json_build_object( 
                    'id', Question.id,
                    'text', Question.q_text,
                    'option1', Question.option1,
                    'option2', Question.option2,
                    'option3', Question.option3,
                    'option4', Question.option4,
                    'correct_answer', Question.correct_answer,
                    'select_answer', cls.select_answer,
                    'is_correct', is_correct,
                    'score', Question.score
                )
            ).label('questions') 
            ).join(User, cls.user_id == User.id
            ).join(Question, cls.q_id == Question.id
            ).group_by(User.id, User.first_name, User.last_name, cls.active
            ).filter(cls.active == 'true').all()

        datas = list(map(lambda x: {
            'user': x.user,
            'questions': x.questions,  
            'active': x.active
        }, data))
        return datas

    @classmethod
    def create(cls, create:list):
        db = cls.db()
        objects = []
        for answer in create:
            db_item = cls(**answer.dict())
            objects.append(db_item)
        db.bulk_save_objects(objects)
        db.commit()
        return objects
    
    @classmethod
    def get_id(cls, user_id: int): 
        db = cls.db()  
        is_correct = case((cls.select_answer == Question.correct_answer, True), else_=False)
        correct_count = func.sum(func.cast(is_correct, Integer))
        data = db.query(
            cls.active.label('active'),
            func.json_build_object(
                'id', User.id,
                'fullname', func.concat(User.first_name, ' ', User.last_name),
                'score_total', correct_count
            ).label('user'),
            func.array_agg(
                func.json_build_object( 
                    'id', Question.id,
                    'text', Question.q_text,
                    'option1', Question.option1,
                    'option2', Question.option2,
                    'option3', Question.option3,
                    'option4', Question.option4,
                    'correct_answer', Question.correct_answer,
                    'select_answer', cls.select_answer,
                    'is_correct', is_correct,
                    'score', Question.score
                )
            ).label('questions') 
            ).join(User, cls.user_id == User.id
            ).join(Question, cls.q_id == Question.id
            ).group_by(User.id, User.first_name, User.last_name, cls.active
            ).filter(cls.user_id == user_id ).all()

        datas = list(map(lambda x: {
            'user': x.user,
            'questions': x.questions,  
            'active': x.active
        }, data))
        return datas