"""auto_generated

Revision ID: fdd959a2cfda
Revises: 
Create Date: 2025-06-01 02:19:26.646342

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fdd959a2cfda'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def create_tab_users():
    op.create_table('users',
                    sa.Column('email', sa.String(length=60), nullable=False),
                    sa.Column('phone', sa.String(length=25), nullable=False),
                    sa.Column('preferred_location', sa.String(length=30), nullable=False),
                    sa.Column('property_types', sa.JSON, nullable=False),
                    sa.Column('budget', sa.String(length=30), nullable=False),
                    sa.Column('request_urgency', sa.String(length=30), nullable=False),

                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('date_created', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('created_by', sa.String(length=36), nullable=True),
                    sa.Column('date_updated', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('updated_by', sa.String(length=36), nullable=True),
                    sa.Column('deleted', sa.Boolean(), nullable=False),
                    sa.Column('date_deleted', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('deleted_by', sa.String(length=36), nullable=True),
                    sa.Column('version', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)


def drop_tab_users():
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')

def upgrade() -> None:
    create_tab_users()


def downgrade() -> None:
    drop_tab_users()
