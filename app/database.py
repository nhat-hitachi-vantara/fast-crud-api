from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:80/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://fastapi:12345678@localhost/db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()