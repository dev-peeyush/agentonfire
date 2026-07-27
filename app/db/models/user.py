from app.db.base import Base
from sqlalchemy.orm import mapped_column, Mapped
import uuid
from ulid import ULID

class User(Base):
    __tablename__='users'
    id:Mapped[str]= mapped_column(unique=True, primary_key=True, index=True, default=lambda:str(ULID()))
    first_name:Mapped[str] = mapped_column(default="first")
    last_name:Mapped[str] = mapped_column(default="last")
    email:Mapped[str] = mapped_column(unique=True, index=True)
    password:Mapped[str] = mapped_column(nullable=False)

    