from sqlalchemy import Column, Integer, String, DATE
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
    date_from = Column(DATE)
    date_to = Column(DATE)
    score = Column(Integer)

    answers = relationship("Answer", back_populates="questions")
   