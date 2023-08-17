from pydantic import BaseModel

class AnswerBase(BaseModel): 
    q_id: int
    user_id: int
    select_answer: str
    is_correct: bool = None
class AnswerCreate(AnswerBase):
    pass
class AnswerUpdate(AnswerBase):
    pass

class Answer(AnswerBase): 
    id: int
    active: bool
    class Config:
        orm_mode = True