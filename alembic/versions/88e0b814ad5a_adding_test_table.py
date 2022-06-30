"""adding test table

Revision ID: 88e0b814ad5a
Revises: 
Create Date: 2022-06-30 11:56:35.917972

"""
from alembic import op
import sqlalchemy as sa

from models import Doi_xe


# revision identifiers, used by Alembic.
revision = '88e0b814ad5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('quan_ly_doi_xe',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('doi_xe',sa.Integer,sa.ForeignKey(Doi_xe.id))
        )


def downgrade():
    op.drop_table('quan_ly_doi_xe')
