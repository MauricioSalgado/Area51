import os


class Config:

    DEBUG = True
    APP_NAME = 'MyCloud'
    SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"