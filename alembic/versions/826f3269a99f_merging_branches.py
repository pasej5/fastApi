"""Merging branches

Revision ID: 826f3269a99f
Revises: 9c1c6bb1bd38
Create Date: 2025-03-09 00:56:44.393769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '826f3269a99f'
down_revision: Union[str, None] = '9c1c6bb1bd38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
