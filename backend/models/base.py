from sqlalchemy import Boolean, Column, Integer
from config.database import Base
from contextlib import contextmanager
from config.database import SessionLocal

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True)

    @classmethod
    def db(cls):
        @contextmanager
        def get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        with get_db() as db:
            return db

    @classmethod
    def get_list(cls):
        data = cls.db().query(cls).filter(cls.active == 'true').all()
        return data
  

    @classmethod
    def get_one(cls, id:int):
        data = cls.db().query(cls).filter(cls.id == id).first()
        return data

    @classmethod
    def create(cls, create):
        db = cls.db()
        data = cls(**create.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @classmethod
    def delete(cls,id: int):
        db = cls.db()
        db_query = db.query(cls).filter(cls.id == id)
        db_delete = db_query.first()
        delete_data = {'active': False}
        db_query.update(delete_data, synchronize_session=False)
        db.commit()
        db.refresh(db_delete)
        return db_delete

    @classmethod
    def update(cls, id: int, update):
        db = cls.db()
        db_query = db.query(cls).filter(cls.id == id)
        db_update = db_query.first()
        update_data = update.dict(exclude_unset=True)
        db_query.filter(cls.id == id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_update)
        return db_update


