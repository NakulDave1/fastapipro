import email
from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    email=Column(String(20),nullable=False)
    password=Column(String(100),nullable=False)

