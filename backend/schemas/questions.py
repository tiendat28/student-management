from pydantic import BaseModel

class QuestionBase(BaseModel): 
    q_text: str
    option1: str
    option2: str
    option3: str
    option4: str
    correct_answer: str
    date_from: str = None
    date_to: str = None
    score: int = None
class QuestionCreate(QuestionBase):
    pass
class QuestionUpdate(QuestionBase):
    pass

class Question(QuestionBase): 
    id: int
    active: bool
    class Config:
        orm_mode = True
