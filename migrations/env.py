# migrations/env.py
from __future__ import with_statement
import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Add the app directory to the system path to import your models
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import your model's Base and User model
from app.db import Base  # Import Base from your app's db.py
from app.accounts.models.user import User  # Import the User model

# This is the Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# This is the target metadata we need to run the migrations
target_metadata = Base.metadata  # This is the MetaData object that Alembic needs

def run_migrations_online():
    # Connect to the database
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Bind the context to the connection
        context.configure(connection=connection, target_metadata=target_metadata)

        # Run migrations
        with context.begin_transaction():
            context.run_migrations()

if __name__ == "__main__":
    run_migrations_online()
