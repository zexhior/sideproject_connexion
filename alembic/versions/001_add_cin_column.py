"""Add cin column to person table

Revision ID: 001_add_cin_column
Revises: 
Create Date: 2026-02-11

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "001_add_cin_column"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('person', sa.Column('cin', sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column('person', 'cin')
