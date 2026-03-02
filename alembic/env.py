"""alembic environment script"""

import os
import sys
import re
from datetime import datetime
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Add the src directory to the path so we can import our models
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from config import url_postgres
from base import Base
import models

def process_revision_directives(context, revision, directives):
    if context.config.get_main_option("revision_environment") == "true":
        script = directives[0]
        now = datetime.now()
        script.rev_id = f"{now.strftime('%Y_%m_%d_%H_%M_%S')}_{now.microsecond // 1000:03d}"

# def generate_sequential_rev_id():
#     versions_dir = os.path.join(os.path.dirname(__file__), "versions")

#     existing = []
#     for filename in os.listdir(versions_dir):
#         match = re.match(r"(\d+)_", filename)
#         if match:
#             existing.append(int(match.group(1)))

#     if not existing:
#         return "001"

#     next_number = max(existing) + 1
#     return f"{next_number:03d}"

# def process_revision_directives(context, revision, directives):
#     script = directives[0]
#     script.rev_id = generate_sequential_rev_id()

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = url_postgres
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = url_postgres

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
