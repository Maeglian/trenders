"""Initial

Revision ID: 10eeac40e511
Revises: 
Create Date: 2019-11-01 20:35:21.800211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10eeac40e511'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'imports',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('clock_timestamp()'), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk__imports'))
    )


def downgrade():
    op.drop_table('imports')
