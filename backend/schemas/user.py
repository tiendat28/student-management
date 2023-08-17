from pydantic import BaseModel

class UserBase(BaseModel):
    username : str
    password : str
    first_name : str
    last_name : str = None
    phone: str = None
    address: str = None
    email : str = None
    sex: str
    role : str

class UserCreate(UserBase):
    pass
class UserUpdate(UserBase):
    pass
class User(UserBase):
    id: int
    active: bool

    class Config:
        orm_mode = True