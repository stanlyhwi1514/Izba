from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Alembic Config object
config = context.config

# Setup loggers from config file if available
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your admin models here
from apis.admin import models
from extensions import db  # Make sure this works with your project structure

target_metadata = db.metadata

# Get DB URI from .env
admin_db_url = os.getenv("SQLALCHEMY_DATABASE_URI")

def run_migrations_online():
    connectable = create_engine(admin_db_url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    raise Exception("Offline mode is not supported.")
else:
    run_migrations_online()
