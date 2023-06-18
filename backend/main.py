from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from config.database import Base, engine, SessionLocal
from models.login import AccountModel
from schemas.login import AccountCreate
from fastapi.middleware.cors import CORSMiddleware
import jwt

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "tiendat2802"

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/login/{id}", tags=["login"])
def read_account(id:str,db: Session = Depends(get_db)):
    account = AccountModel.get_account(db,id)
    token = jwt.encode({'id': account.id}, SECRET_KEY, algorithm='HS256')
    account.token = token
    return {
        "token": account.token
    }

@app.get("/login/" , tags=["login"])
def read_accounts(db: Session = Depends(get_db)):
    accounts = AccountModel.get_accounts(db=db)
    for account in accounts:
        token = jwt.encode({'id': account.id}, SECRET_KEY, algorithm='HS256')
        account.token = token
    return accounts

@app.post("/login/", tags=["login"])
def create_account(create:AccountCreate, db: Session = Depends(get_db)):
    cre_account = AccountModel.create_account(db=db, create=create)
    token = jwt.encode({'id': cre_account.id}, SECRET_KEY, algorithm='HS256')
    cre_account.token = token
    return {
        "token": cre_account.token 
    }

@app.delete("/login/{id}", tags=["login"])
def delete_account(id: str, db: Session = Depends(get_db)):
    account_model = AccountModel()
    deleted_account = account_model.delete_account( id=id, db=db)
    return deleted_account