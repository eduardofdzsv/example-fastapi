"""add user table

Revision ID: 89b289ad8032
Revises: 9366388fe175
Create Date: 2022-07-27 14:12:20.682402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89b289ad8032'
down_revision = '9366388fe175'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass

def downgrade():
    op.drop_table('users')
    pass