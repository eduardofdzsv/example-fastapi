"""create posts table

Revision ID: 5e8c68b7a35c
Revises: 
Create Date: 2022-07-27 08:46:45.400253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e8c68b7a35c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
        )
    pass


def downgrade():
    op.drop_table('posts')
    pass
