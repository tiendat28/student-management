from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.base import BaseModel

class User(BaseModel):
    __tablename__ = "user"

    username = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String, unique=True)
    address = Column(String)
    email = Column(String, unique=True)
    sex = Column(String)
    role = Column(String)
   
    student = relationship("Student", back_populates="user")
    teacher = relationship("Teacher", back_populates="user")
    answers = relationship("Answer", back_populates="user")


    @classmethod
    def auther_user(cls, username: str, password: str):
        user = cls.db().query(cls).filter(cls.username == username and cls.password == password).first()
        if not user:
            return None
        return user