import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Configuración de Alembic
config = context.config
fileConfig(config.config_file_name)

# Cargar las variables de entorno para la URL de la base de datos
database_url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user=os.getenv("PSQL_USER", "postgres"),
    password=os.getenv("PSQL_PSW", "abc123."),
    host=os.getenv("PSQL_HOST", "db"),
    port=os.getenv("PSQL_PORT", "5432"),
    database=os.getenv("PSQL_DB", "vacasgal"),
)
config.set_main_option("sqlalchemy.url", database_url)

# Agregar la metadata de los modelos
from app import create_app
from extensions import db

flask_app = create_app()
flask_app.app_context().push()

target_metadata = db.metadata

def run_migrations_offline():
    """Ejecuta las migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta las migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
