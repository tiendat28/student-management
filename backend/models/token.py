import jwt
from models.base import BaseModel

SECRET_KEY = "tiendat2802"
ALGORITHM='HS256'


class Token(BaseModel):
    __abstract__ = True
    
    @classmethod
    def create_token(cls, data: dict):
        encode_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return encode_jwt
