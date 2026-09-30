from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# load all models from modules
# importing all the variables form config file
from env import DATABASE_URL

# Calling the Base from DB config file to check and detect the DB pool and models for migrations
from infrastructure.database import Base

# This one is for the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config
safe_url = DATABASE_URL.replace("%", "%%")

config.set_main_option("sqlalchemy.url", safe_url)

# This will configure logging, so that all the log messages from the migration process are captured and outputted.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    This one is configures the context with in just URL
    and not an Engine, though an Engine is still needed to generate the SQL statements.
    we don't want a DBAPI to be available.

    calling the context.execute() here to emit the given string to the script output.

    """

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migration_online() -> None:
    """Run migrations in 'online' mode.
    In this one we create an Engine and associate a connection with the context.

    """

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migration_online()
