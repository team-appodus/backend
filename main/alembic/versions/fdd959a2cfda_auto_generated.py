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

def create_tab_projects():
    op.create_table('projects',
                    sa.Column('fullname', sa.String(length=100), nullable=False),
                    sa.Column('email', sa.String(length=60), nullable=False),
                    sa.Column('phone', sa.String(length=17), nullable=False),
                    sa.Column('company_name', sa.String(length=100), nullable=False),
                    sa.Column('budget', sa.String(length=100), nullable=False),
                    sa.Column('timeline', sa.String(length=100), nullable=False),
                    sa.Column('what_building', sa.Text, nullable=False),
                    sa.Column('what_not_building', sa.Text, nullable=False),
                    sa.Column('build_summary', sa.Text, nullable=True),
                    sa.Column('customer_location', sa.String(length=30), nullable=False),
                    sa.Column('build_type', sa.String(length=30), nullable=False),
                    sa.Column('platform', sa.String(length=30), nullable=False),
                    sa.Column('core_product_types', sa.JSON(), nullable=True),
                    sa.Column('web_presences', sa.JSON(), nullable=True),
                    sa.Column('growth_and_sales', sa.JSON(), nullable=True),
                    sa.Column('community_and_engagements', sa.JSON(), nullable=True),
                    sa.Column('learning_and_onboardings', sa.JSON(), nullable=True),
                    sa.Column('payments', sa.JSON(), nullable=True),
                    sa.Column('escrow_support', sa.Boolean(), nullable=True),
                    sa.Column('messaging_apis', sa.JSON(), nullable=True),
                    sa.Column('ai_model_apis', sa.JSON(), nullable=True),
                    sa.Column('social_logins', sa.JSON(), nullable=True),
                    sa.Column('other_social_logins', sa.JSON(), nullable=True),
                    sa.Column('file_stores', sa.JSON(), nullable=True),
                    sa.Column('other_file_stores', sa.String(length=100), nullable=True),
                    sa.Column('marketing_tools', sa.String(length=100), nullable=True),
                    sa.Column('other_third_party_apis', sa.String(length=100), nullable=True),
                    sa.Column('post_production_support', sa.Integer(), nullable=False),
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('date_created', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('created_by', sa.String(length=36), nullable=True),
                    sa.Column('date_updated', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('updated_by', sa.String(length=36), nullable=True),
                    sa.Column('deleted', sa.Boolean(), nullable=False),
                    sa.Column('date_deleted', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('deleted_by', sa.String(length=36), nullable=True),
                    sa.Column('version', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_projects_deleted'), 'projects', ['deleted'], unique=False)
    op.create_index(op.f('ix_projects_id'), 'projects', ['id'], unique=True)
def drop_tab_projects():
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    op.drop_index(op.f('ix_projects_deleted'), table_name='projects')
    op.drop_table('projects')

def create_tab_projects_staging():
    op.create_table('projects_staging',
                    sa.Column('fullname', sa.String(length=100), nullable=False),
                    sa.Column('email', sa.String(length=60), nullable=False),
                    sa.Column('phone', sa.String(length=17), nullable=False),
                    sa.Column('company_name', sa.String(length=100), nullable=False),
                    sa.Column('budget', sa.String(length=100), nullable=True),
                    sa.Column('timeline', sa.String(length=100), nullable=True),
                    sa.Column('what_building', sa.Text, nullable=True),
                    sa.Column('what_not_building', sa.Text, nullable=True),
                    sa.Column('build_summary', sa.Text, nullable=True),
                    sa.Column('customer_location', sa.String(length=30), nullable=True),
                    sa.Column('build_type', sa.String(length=30), nullable=True),
                    sa.Column('platform', sa.String(length=30), nullable=True),
                    sa.Column('core_product_types', sa.JSON(), nullable=True),
                    sa.Column('web_presences', sa.JSON(), nullable=True),
                    sa.Column('growth_and_sales', sa.JSON(), nullable=True),
                    sa.Column('community_and_engagements', sa.JSON(), nullable=True),
                    sa.Column('learning_and_onboardings', sa.JSON(), nullable=True),
                    sa.Column('payments', sa.JSON(), nullable=True),
                    sa.Column('escrow_support', sa.Boolean(), nullable=True),
                    sa.Column('messaging_apis', sa.JSON(), nullable=True),
                    sa.Column('ai_model_apis', sa.JSON(), nullable=True),
                    sa.Column('social_logins', sa.JSON(), nullable=True),
                    sa.Column('other_social_logins', sa.JSON(), nullable=True),
                    sa.Column('file_stores', sa.JSON(), nullable=True),
                    sa.Column('other_file_stores', sa.String(length=100), nullable=True),
                    sa.Column('marketing_tools', sa.String(length=100), nullable=True),
                    sa.Column('other_third_party_apis', sa.String(length=100), nullable=True),
                    sa.Column('post_production_support', sa.Integer(), nullable=True),
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('date_created', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('created_by', sa.String(length=36), nullable=True),
                    sa.Column('date_updated', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('updated_by', sa.String(length=36), nullable=True),
                    sa.Column('deleted', sa.Boolean(), nullable=False),
                    sa.Column('date_deleted', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('deleted_by', sa.String(length=36), nullable=True),
                    sa.Column('version', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_projects_staging_deleted'), 'projects_staging', ['deleted'], unique=False)
    op.create_index(op.f('ix_projects_staging_id'), 'projects_staging', ['id'], unique=True)
def drop_tab_projects_staging():
    op.drop_index(op.f('ix_projects_staging_id'), table_name='projects_staging')
    op.drop_index(op.f('ix_projects_staging_deleted'), table_name='projects_staging')
    op.drop_table('projects_staging')
    
def upgrade() -> None:
    create_tab_projects()
    create_tab_projects_staging()


def downgrade() -> None:
    drop_tab_projects()
    drop_tab_projects_staging()
