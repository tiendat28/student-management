from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# DATABASE_URL = f"postgresql://{postgres}:{postgres}@{db}:{5432}/{default}"

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    f"postgresql://postgres:280200@localhost:5432/studentmanager"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()