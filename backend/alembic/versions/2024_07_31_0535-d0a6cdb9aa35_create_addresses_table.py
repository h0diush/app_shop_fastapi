"""create addresses table

Revision ID: d0a6cdb9aa35
Revises: 3a6603a9f52b
Create Date: 2024-07-31 05:35:39.473328

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d0a6cdb9aa35"
down_revision: Union[str, None] = "3a6603a9f52b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "addresses",
        sa.Column(
            "city",
            sa.String(length=18),
            nullable=False,
        ),
        sa.Column("street", sa.String(length=28), nullable=False),
        sa.Column("home", sa.Integer(), nullable=False),
        sa.Column("room", sa.Integer(), nullable=True),
        sa.Column("entrance", sa.Integer(), nullable=True),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
            name=op.f("fk_addresses_profile_id_profiles"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_addresses")),
    )


def downgrade() -> None:
    op.drop_table("addresses")
