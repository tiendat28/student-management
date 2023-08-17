from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BaseModel

class Answer(BaseModel):
    __tablename__ = "answers"

    q_id = Column(Integer, ForeignKey("questions.id"))
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    select_answer = Column(String)
    is_correct = Column(Boolean)

    questions = relationship("Question", back_populates="answers")
    user = relationship("User", back_populates="answers")

    
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