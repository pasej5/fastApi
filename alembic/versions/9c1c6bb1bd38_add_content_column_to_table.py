"""add content column to table

Revision ID: 9c1c6bb1bd38
Revises: 4541ffd260e5
Create Date: 2025-03-08 23:38:10.269750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c1c6bb1bd38'
down_revision: Union[str, None] = '4541ffd260e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass