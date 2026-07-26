from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


db_engine = create_engine(
    url=settings.DATABASE_URI
)

db_session = sessionmaker(
    bind= db_engine,
    autoflush=False,
)


def get_db():
    db = db_session()
    print("get_db")
    try:
        yield db
    finally:
        db.close()
