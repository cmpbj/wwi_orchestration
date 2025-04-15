from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import create_engine
from airflow.hooks.base import BaseHook

conn = BaseHook.get_connection("wwi_postgres_connection")
raw_uri = conn.get_uri()
# Replace 'postgres://' with 'postgresql://' manually
POSTGRES_DATABASE_URL = raw_uri.replace("postgres://", "postgresql://")

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
