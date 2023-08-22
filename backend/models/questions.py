from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import BaseModel

class Question(BaseModel):
    __tablename__ = "questions"

    q_text = Column(String)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    option4 = Column(String)
    correct_answer = Column(String)
    date_from = Column(String)
    date_to = Column(String)
    score = Column(Integer)

    answers = relationship("Answer", back_populates="questions")
   