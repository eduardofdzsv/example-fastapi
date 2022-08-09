"""add content column to posts table

Revision ID: 9366388fe175
Revises: 5e8c68b7a35c
Create Date: 2022-07-27 11:17:32.436004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9366388fe175'
down_revision = '5e8c68b7a35c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
