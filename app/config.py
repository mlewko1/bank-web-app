import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "tajny-klucz"
    SQLALCHEMY_DATABASE_URI = "sqlite:///bank.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
