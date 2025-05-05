from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from extensions import db
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# Ensure your models are imported so Alembic sees them
from apis.Users import models
from apis.customers import models
from apis.vendors import models
from apis.initiators import models


# Get tenant databases from environment variables
tenant_databases = os.getenv("TENANT_DATABASES")
tenant_databases = eval(tenant_databases)  # Convert string to dictionary


# Alembic config
config = context.config
if config.config_file_name is not None:
   fileConfig(config.config_file_name)


# Function to get engine dynamically for each tenant
def get_engine(db_url):
   return create_engine(db_url)


# Migration runner function
def run_migrations_online():
   for tenant_name, db_url in tenant_databases.items():
       print(f"Running migrations for {tenant_name} database...")


       # Set up the engine and connection for the current tenant
       connectable = get_engine(db_url)


       # Run migrations for this tenant's database
       with connectable.connect() as connection:
           context.configure(connection=connection, target_metadata=db.metadata)


           with context.begin_transaction():
               context.run_migrations()


# Run migrations
if context.is_offline_mode():
   print("Running migrations offline mode is not supported.")
else:
   run_migrations_online()



