"""empty message

Revision ID: 44df3a462448
Revises: e46011c750b2
Create Date: 2017-12-27 20:49:39.179473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44df3a462448'
down_revision = 'e46011c750b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('remarks', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goods', 'remarks')
    # ### end Alembic commands ###
