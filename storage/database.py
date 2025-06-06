from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///bank.db")
SessionLocal = sessionmaker(bind=engine)


def init_db():
    from models.account import Account

    Base.metadata.create_all(engine)
