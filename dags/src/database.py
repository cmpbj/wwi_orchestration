from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import create_engine

POSTGRES_DATABASE_URL = "postgresql://user:K7414MaAeOWhq8YQP8TYpk3mxpOej19f@dpg-cvijik1r0fns738g95k0-a.oregon-postgres.render.com:5432/sales_db_rxft"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()