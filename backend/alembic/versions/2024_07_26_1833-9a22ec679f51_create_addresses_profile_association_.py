"""create addresses_profile_association table

Revision ID: 9a22ec679f51
Revises: 04e4e340c4f2
Create Date: 2024-07-26 18:33:26.643560

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9a22ec679f51"
down_revision: Union[str, None] = "04e4e340c4f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "address_profile_association",
        sa.Column(
            "profile_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column("address_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["address_id"],
            ["addresses.id"],
            name=op.f(
                "fk_address_profile_association_address_id_addresses",
            ),
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
            name=op.f("fk_address_profile_association_profile_id_profiles"),
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f(
                "pk_address_profile_association",
            ),
        ),
    )


def downgrade() -> None:
    op.drop_table("address_profile_association")
