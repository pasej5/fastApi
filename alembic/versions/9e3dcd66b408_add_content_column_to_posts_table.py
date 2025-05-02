"""add content column to posts table

Revision ID: 9e3dcd66b408
Revises: fcd94a15e83d
Create Date: 2025-05-03 01:06:21.814280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e3dcd66b408'
down_revision: Union[str, None] = 'fcd94a15e83d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass