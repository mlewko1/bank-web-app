import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "bank.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "tajny-klucz-do-aplikacji"
