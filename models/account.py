from sqlalchemy import Column, Integer, String, Float
from storage.database import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    balance = Column(Float)