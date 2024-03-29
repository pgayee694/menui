"""added location table and cleaned up others

Revision ID: 3fdedbd6a588
Revises: 7546857c977e
Create Date: 2019-10-29 23:01:56.456231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fdedbd6a588'
down_revision = '7546857c977e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('region', sa.String(length=64), nullable=False),
    sa.Column('country', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.drop_table('user_restaurant')
    op.create_table('user_restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.drop_table('friends')
    op.create_table('friends',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('friend1_id', sa.Integer(), nullable=False),
    sa.Column('friend2_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['friend1_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['friend2_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.drop_table('restaurant')
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.drop_table('user')
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('user', 'location',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('restaurant', 'name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('friends', 'friend2_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('friends', 'friend1_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_table('user_restaurants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('restaurant_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_restaurant')
    op.drop_table('location')
    # ### end Alembic commands ###
