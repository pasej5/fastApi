"""add foreign-key to post table

Revision ID: 3e8e7741f41a
Revises: 48f62c2aa4a0
Create Date: 2025-03-09 00:18:19.322596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e8e7741f41a'
down_revision: Union[str, None] = '4541ffd260e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('own_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['own_id'], remote_cols=['id'], ondelete=CASCADE)
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
