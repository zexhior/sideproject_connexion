"""Script to apply Alembic migrations."""

from alembic.config import Config
from alembic.command import upgrade

def apply_migrations():
    """Apply pending migrations to the database."""
    alembic_cfg = Config("alembic.ini")
    upgrade(alembic_cfg, "head")
    print("Migrations appliquées avec succès!")

if __name__ == "__main__":
    apply_migrations()
