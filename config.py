import os,json
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    ENV = os.getenv("APP_ENV", "development")  # "development" or "production"
    DEBUG = ENV == "development"
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # The DB URI will be loaded from .env file
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    MONGO_URI = os.getenv("MONGO_URI")

    
    # For tenant databases
    TENANT_DATABASES = json.loads(os.getenv("TENANT_DATABASES", "{}"))
    TENANT_MONGODB_URIS = json.loads(os.getenv("TENANT_MONGODB_URIS", "{}"))

    # Make sure to convert to the appropriate type (integer or boolean)
    SQLALCHEMY_POOL_SIZE = int(os.getenv("SQLALCHEMY_POOL_SIZE", 5))  # Default 5
    SQLALCHEMY_MAX_OVERFLOW = int(os.getenv("SQLALCHEMY_MAX_OVERFLOW", 10))  # Default 10
    SQLALCHEMY_POOL_PRE_PING = os.getenv("SQLALCHEMY_POOL_PRE_PING", "True") == "True"  # Default True
