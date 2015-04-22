"""initial migration

Revision ID: 476fd0e40f04
Revises: a47c9c28e72
Create Date: 2015-04-22 18:57:20.782836

"""

# revision identifiers, used by Alembic.
revision = '476fd0e40f04'
down_revision = 'a47c9c28e72'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('single_choice', sa.String(length=255), nullable=True),
    sa.Column('blank_fill', sa.String(length=255), nullable=True),
    sa.Column('essay', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_paper')
    ### end Alembic commands ###
