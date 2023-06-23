from pydantic import BaseModel

class AccountBase(BaseModel):
    name: str
    surname: str
    users: str
    password: str
    email: str
    role: str

class AccountCreate(AccountBase):
    active: bool

class AccountDelete(AccountBase):
    pass

class Account(AccountBase):
    id: int
    class Config:
        orm_mode = True