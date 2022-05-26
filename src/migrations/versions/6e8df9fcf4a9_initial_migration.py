"""Initial migration.

Revision ID: 6e8df9fcf4a9
Revises: 
Create Date: 2022-05-25 22:35:07.454968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e8df9fcf4a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('publisher', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_publisher'), 'books', ['publisher'], unique=False)
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('src_page', sa.Integer(), nullable=True),
    sa.Column('submodel', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entries_title'), 'entries', ['title'], unique=False)
    op.create_table('traits',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('actions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trigger', sa.Text(), nullable=True),
    sa.Column('requirements', sa.Text(), nullable=True),
    sa.Column('action_type', sa.Enum('reaction', 'action', 'free_action', 'activity', name='actiontype'), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['entries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hazards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('is_complex', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['entries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hazards_level'), 'hazards', ['level'], unique=False)
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['entries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rel_entries_sourcebooks',
    sa.Column('entry_id', sa.Integer(), nullable=True),
    sa.Column('src_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entries.id'], ),
    sa.ForeignKeyConstraint(['src_id'], ['books.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rel_entries_sourcebooks')
    op.drop_table('items')
    op.drop_index(op.f('ix_hazards_level'), table_name='hazards')
    op.drop_table('hazards')
    op.drop_table('actions')
    op.drop_table('traits')
    op.drop_index(op.f('ix_entries_title'), table_name='entries')
    op.drop_table('entries')
    op.drop_index(op.f('ix_books_publisher'), table_name='books')
    op.drop_table('books')
    # ### end Alembic commands ###
