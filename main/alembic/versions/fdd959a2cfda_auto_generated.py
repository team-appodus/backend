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
                    sa.Column('budget_range', sa.String(length=100), nullable=False),
                    sa.Column('timeline', sa.String(length=100), nullable=False),
                    sa.Column('what_building', sa.Text, nullable=False),
                    sa.Column('what_not_building', sa.Text, nullable=False),
                    sa.Column('build_summary', sa.Text, nullable=True),
                    sa.Column('customer_location', sa.String(length=30), nullable=False),
                    sa.Column('build_type', sa.String(length=30), nullable=False),
                    sa.Column('platform', sa.String(length=30), nullable=False),
                    sa.Column('product_types', sa.JSON(), nullable=True),
                    sa.Column('payments', sa.JSON(), nullable=True),
                    sa.Column('escrow_support', sa.Boolean(), nullable=True),
                    sa.Column('messaging_apis', sa.JSON(), nullable=True),
                    sa.Column('ai_model_apis', sa.JSON(), nullable=True),
                    sa.Column('social_logins', sa.JSON(), nullable=True),
                    sa.Column('other_social_logins', sa.JSON(), nullable=True),
                    sa.Column('file_stores', sa.JSON(), nullable=True),
                    sa.Column('other_file_stores', sa.String(length=100), nullable=True),
                    sa.Column('crm_tools', sa.String(length=100), nullable=True),
                    sa.Column('other_third_party_apis', sa.String(length=100), nullable=True),
                    sa.Column('post_production_support', sa.String(length=10), nullable=False),
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
                    sa.Column('budget_range', sa.String(length=100), nullable=True),
                    sa.Column('timeline', sa.String(length=100), nullable=True),
                    sa.Column('what_building', sa.Text, nullable=True),
                    sa.Column('what_not_building', sa.Text, nullable=True),
                    sa.Column('build_summary', sa.Text, nullable=True),
                    sa.Column('customer_location', sa.String(length=30), nullable=True),
                    sa.Column('build_type', sa.String(length=30), nullable=True),
                    sa.Column('platform', sa.String(length=30), nullable=True),
                    sa.Column('product_types', sa.JSON(), nullable=True),
                    sa.Column('payments', sa.JSON(), nullable=True),
                    sa.Column('escrow_support', sa.Boolean(), nullable=True),
                    sa.Column('messaging_apis', sa.JSON(), nullable=True),
                    sa.Column('ai_model_apis', sa.JSON(), nullable=True),
                    sa.Column('social_logins', sa.JSON(), nullable=True),
                    sa.Column('other_social_logins', sa.JSON(), nullable=True),
                    sa.Column('file_stores', sa.JSON(), nullable=True),
                    sa.Column('other_file_stores', sa.String(length=100), nullable=True),
                    sa.Column('crm_tools', sa.String(length=100), nullable=True),
                    sa.Column('other_third_party_apis', sa.String(length=100), nullable=True),
                    sa.Column('post_production_support', sa.String(length=10), nullable=True),
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

def create_tab_addresses():
    op.create_table('addresses',
                    sa.Column('user_id', sa.String(length=36), nullable=False),
                    sa.Column('street_number', sa.String(length=10), nullable=False),
                    sa.Column('street_name', sa.String(length=40), nullable=False),
                    sa.Column('neighborhood', sa.String(length=20), nullable=False),
                    sa.Column('locality', sa.String(length=20), nullable=False),
                    sa.Column('lga', sa.String(length=36), nullable=False),
                    sa.Column('state', sa.String(length=36), nullable=False),
                    sa.Column('country_id', sa.String(length=36), nullable=False),
                    sa.Column('gps_location', sa.JSON(), nullable=False),
                    sa.Column('verified', sa.Boolean(), nullable=False),
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
    op.create_index(op.f('ix_addresses_deleted'), 'addresses', ['deleted'], unique=False)
    op.create_index(op.f('ix_addresses_id'), 'addresses', ['id'], unique=True)
    op.create_index(op.f('ix_addresses_user_id'), 'addresses', ['user_id'], unique=False)
def drop_tab_addresses():
    op.drop_index(op.f('ix_addresses_user_id'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_id'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_deleted'), table_name='addresses')
    op.drop_table('addresses')

def create_tab_devices():
    op.create_table('devices',
                    sa.Column('user_id', sa.String(length=36), nullable=False),
                    sa.Column('device_id', sa.String(length=36), nullable=False),
                    sa.Column('push_provider_type', sa.String(length=20), nullable=False),
                    sa.Column('push_token', sa.JSON(), nullable=False),
                    sa.Column('last_active', sa.DateTime(), nullable=False),
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
    op.create_index(op.f('ix_devices_deleted'), 'devices', ['deleted'], unique=False)
    op.create_index(op.f('ix_devices_id'), 'devices', ['id'], unique=True)
def drop_tab_devices():
    op.drop_table('devices')
    op.drop_index(op.f('ix_chatbots_id'), table_name='chatbots')
    op.drop_index(op.f('ix_chatbots_deleted'), table_name='chatbots')

def create_tab_key_values():
    op.create_table('key_values',
                    sa.Column('key', sa.String(length=128), nullable=False),
                    sa.Column('value', sa.LargeBinary(), nullable=False),
                    sa.Column('expires_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('key')
                    )
    op.create_index(op.f('ix_key_values_key'), 'key_values', ['key'], unique=True)
def drop_tab_key_values():
    op.drop_index(op.f('ix_key_values_key'), table_name='key_values')
    op.drop_table('key_values')

def create_tab_users():
    op.create_table('users',
                    sa.Column('email', sa.String(length=60), nullable=False),
                    sa.Column('phone', sa.String(length=25), nullable=True),
                    sa.Column('phone_ext', sa.String(length=6), nullable=True),
                    sa.Column('password', sa.String(length=512), nullable=True),
                    sa.Column('password_last_updated', sa.DateTime(), nullable=True),
                    sa.Column('firstname', sa.String(length=30), nullable=False),
                    sa.Column('middle_name', sa.String(length=30), nullable=True),
                    sa.Column('lastname', sa.String(length=30), nullable=False),
                    sa.Column('user_type', sa.String(length=2), nullable=False),
                    sa.Column('status', sa.String(length=12), nullable=False),
                    sa.Column('dob', sa.Date(), nullable=True),
                    sa.Column('gender', sa.String(length=2), nullable=True),
                    sa.Column('last_active_date', sa.DateTime(), nullable=True),
                    sa.Column('notes', sa.Text(), nullable=True),
                    sa.Column('profile_picture_doc_id', sa.String(length=36), nullable=True),
                    sa.Column('selfie_picture_doc_id', sa.String(length=36), nullable=True),
                    sa.Column('bvn', sa.String(length=40), nullable=True),
                    sa.Column('bvn_validated', sa.Boolean(), nullable=False),
                    sa.Column('phone_validated', sa.Boolean(), nullable=False),
                    sa.Column('email_validated', sa.Boolean(), nullable=False),
                    sa.Column('identity_validated', sa.Boolean(), nullable=False),
                    sa.Column('address_id', sa.String(length=36), nullable=True),
                    sa.Column('address_validated', sa.Boolean(), nullable=False),
                    sa.Column('selfie_validated', sa.Boolean(), nullable=False),
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
    op.create_index(op.f('ix_users_deleted'), 'users', ['deleted'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
def drop_tab_users():
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_deleted'), table_name='users')
    op.drop_table('users')
    
def upgrade() -> None:
    create_tab_projects()
    create_tab_projects_staging()
    create_tab_addresses()
    create_tab_devices()
    create_tab_key_values()
    create_tab_users()


def downgrade() -> None:
    drop_tab_projects()
    drop_tab_projects_staging()
    drop_tab_addresses()
    drop_tab_devices()
    drop_tab_key_values()
    drop_tab_users()
