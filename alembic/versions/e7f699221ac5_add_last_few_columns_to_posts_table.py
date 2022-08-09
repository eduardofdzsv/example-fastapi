"""add last few columns to posts table

Revision ID: e7f699221ac5
Revises: cedd8b0f8005
Create Date: 2022-07-28 10:32:19.189089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7f699221ac5'
down_revision = 'cedd8b0f8005'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
        sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=
        sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
