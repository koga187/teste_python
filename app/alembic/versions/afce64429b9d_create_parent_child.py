"""empty message

Revision ID: afce64429b9d
Revises:
Create Date: 2023-07-10 12:58:32.041030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "afce64429b9d"
down_revision = None
branch_labels = None
depends_on = None


def downgrade() -> None:
    op.drop_index("ix_parents_id", table_name="parents")
    op.drop_index("ix_parents_name", table_name="parents")
    op.drop_table("parents")
    op.drop_index("ix_children_id", table_name="children")
    op.drop_index("ix_children_name", table_name="children")
    op.drop_table("children")


def upgrade() -> None:
    op.create_table(
        "parents",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "name",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="parents_pkey"),
    )
    op.create_index("ix_parents_name", "parents", ["name"], unique=False)
    op.create_index("ix_parents_id", "parents", ["id"], unique=False)
    op.create_table(
        "children",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "name",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "parent_id",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["parent_id"], ["parents.id"], name="children_parent_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="children_pkey"),
    )
    op.create_index("ix_children_name", "children", ["name"], unique=False)
    op.create_index("ix_children_id", "children", ["id"], unique=False)
