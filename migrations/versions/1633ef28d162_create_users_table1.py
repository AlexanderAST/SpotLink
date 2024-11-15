"""create users table1

Revision ID: 1633ef28d162
Revises: c63109f8ba8a
Create Date: 2024-11-15 13:57:43.913051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1633ef28d162'
down_revision: Union[str, None] = 'c63109f8ba8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
