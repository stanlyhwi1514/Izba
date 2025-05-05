from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from register_blueprints import register_blueprints
from middleware import register_middleware
from extensions import db,mongo

migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    
    # Load config from Config class
    app.config.from_object(Config)

    # Register blueprints and middleware
    register_blueprints(app)
    db.init_app(app)
    mongo.init_app(app)
    migrate.init_app(app, db)
    register_middleware(app)
    
    return app
