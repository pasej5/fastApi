"""add cntent column to posts table

Revision ID: fcd94a15e83d
Revises: 2da7a70708a0
Create Date: 2025-05-03 01:00:20.486526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcd94a15e83d'
down_revision: Union[str, None] = '2da7a70708a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
