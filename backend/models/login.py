from entities.login import Account
from sqlalchemy.orm import Session
from schemas.login import AccountCreate

class AccountModel:
    _entity = Account
    @classmethod
    
    def get_account(cls, db: Session, id: int):

        return db.query(Account).filter(Account.id == id).first()

    def get_accounts(db: Session):

        return db.query(Account).all() 

    def create_account(db: Session, create:AccountCreate):
        db_create = Account(name = create.name, surname = create.surname, users=create.users, password=create.password, email=create.email, role=create.role, active=create.active)
        db.add(db_create)
        db.commit()
        db.refresh(db_create)
        return db_create
    
    def delete_account(self,id: str, db: Session ):
        db_query = db.query(Account).filter(Account.id == id)
        db_delete = db_query.first()
        delete_data = {'active': False}
        db_query.update(delete_data, synchronize_session=False)
        db.commit()
        db.refresh(db_delete)
        return db_delete