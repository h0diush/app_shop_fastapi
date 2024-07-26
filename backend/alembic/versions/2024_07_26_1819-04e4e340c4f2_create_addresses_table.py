"""create addresses table

Revision ID: 04e4e340c4f2
Revises: 3a6603a9f52b
Create Date: 2024-07-26 18:19:34.976463

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "04e4e340c4f2"
down_revision: Union[str, None] = "3a6603a9f52b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "addresses",
        sa.Column("city", sa.String(length=18), nullable=False),
        sa.Column("street", sa.String(length=28), nullable=False),
        sa.Column("home", sa.Integer(), nullable=False),
        sa.Column("room", sa.Integer(), nullable=True),
        sa.Column("entrance", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_addresses")),
    )


def downgrade() -> None:
    op.drop_table("addresses")
