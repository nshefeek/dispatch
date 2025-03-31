"""adds snooze extension oncall service to project

Revision ID: bccbf255d6d1
Revises: 92a359040b8e
Create Date: 2025-03-28 13:12:07.514337

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bccbf255d6d1"
down_revision = "92a359040b8e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project", sa.Column("snooze_extension_oncall_service_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None, "project", "service", ["snooze_extension_oncall_service_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "project", type_="foreignkey")
    op.drop_column("project", "snooze_extension_oncall_service_id")
    # ### end Alembic commands ###
