"""cascade in address_profile_association

Revision ID: 2a63aa655f80
Revises: 9a22ec679f51
Create Date: 2024-07-29 20:09:06.064228

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a63aa655f80"
down_revision: Union[str, None] = "9a22ec679f51"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "fk_address_profile_association_profile_id_profiles",
        "address_profile_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        "fk_address_profile_association_address_id_addresses",
        "address_profile_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_address_profile_association_profile_id_profiles"),
        "address_profile_association",
        "profiles",
        ["profile_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_address_profile_association_address_id_addresses"),
        "address_profile_association",
        "addresses",
        ["address_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_address_profile_association_address_id_addresses"),
        "address_profile_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_address_profile_association_profile_id_profiles"),
        "address_profile_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_address_profile_association_address_id_addresses",
        "address_profile_association",
        "addresses",
        ["address_id"],
        ["id"],
    )
    op.create_foreign_key(
        "fk_address_profile_association_profile_id_profiles",
        "address_profile_association",
        "profiles",
        ["profile_id"],
        ["id"],
    )
