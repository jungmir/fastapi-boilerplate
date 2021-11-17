"""create user table

Revision ID: 638c68488b1c
Revises: 
Create Date: 2021-11-17 23:21:41.747715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638c68488b1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('user_id', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
        sa.Column('nickname', sa.String, unique=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('phone', sa.String),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.func.now(), nullable=False)
    )


def downgrade():
    op.drop_table('users')
