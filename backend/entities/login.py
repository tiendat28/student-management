from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base



class Account(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    users = Column(String)
    password = Column(String)
    surname = Column(String)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    active = Column(Boolean)