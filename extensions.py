from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_pymongo import PyMongo


db = SQLAlchemy(engine_options={
    "pool_size": Config.SQLALCHEMY_POOL_SIZE,
    "max_overflow": Config.SQLALCHEMY_MAX_OVERFLOW,
    "pool_pre_ping": Config.SQLALCHEMY_POOL_PRE_PING
})

mongo = PyMongo()
