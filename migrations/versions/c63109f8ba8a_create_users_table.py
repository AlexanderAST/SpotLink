"""create users table

Revision ID: c63109f8ba8a
Revises: bd525896310e
Create Date: 2024-11-15 13:55:09.530012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c63109f8ba8a'
down_revision: Union[str, None] = 'bd525896310e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
