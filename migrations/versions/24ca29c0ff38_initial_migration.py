"""initial migration

Revision ID: 24ca29c0ff38
Revises: 4874d58c818
Create Date: 2015-04-14 15:15:14.610934

"""

# revision identifiers, used by Alembic.
revision = '24ca29c0ff38'
down_revision = '4874d58c818'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('points',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('points')
    ### end Alembic commands ###