"""create profiles tables

Revision ID: 3a6603a9f52b
Revises: 412c6d6cfaf2
Create Date: 2024-07-25 21:32:36.921599

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "3a6603a9f52b"
down_revision: Union[str, None] = "412c6d6cfaf2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "profiles",
        sa.Column(
            "first_name",
            sa.String(length=24),
            nullable=False,
        ),
        sa.Column(
            "last_name",
            sa.String(length=24),
            nullable=False,
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("phone", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f(
                "fk_profiles_user_id_users",
            ),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_profiles")),
        sa.UniqueConstraint(
            "user_id",
            name=op.f("uq_profiles_user_id"),
        ),
    )


def downgrade() -> None:
    op.drop_table("profiles")
