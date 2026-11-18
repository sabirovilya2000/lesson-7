"""Add status column
Revision ID: abcdef123456
Revises: 123456789abc
"""
from alembic import op
import sqlalchemy as sa

revision = 'abcdef123456'
down_revision = '123456789abc'

def upgrade():
    op.add_column('orders', sa.Column('status', sa.String(length=20), nullable=False, server_default='pending'))

def downgrade():
    op.drop_column('orders', 'status')