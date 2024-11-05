"""add post_season column to Season model

Revision ID: d93604c4f522
Revises: d580b890f7bd
Create Date: 2024-11-04 17:34:13.136686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd93604c4f522'
down_revision: Union[str, None] = 'd580b890f7bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Season')
    op.drop_table('Player')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Player',
    sa.Column('player_id', sa.INTEGER(), server_default=sa.text('nextval(\'"Player_player_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('birthdate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('player_headshot_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('height', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('weight', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('years_in_league', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('player_id', name='Player_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Season',
    sa.Column('season_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('player_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('year', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('GP', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('MIN', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('PTS', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('REB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AST', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('STL', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('BLK', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FGM', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FGA', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FG_PCT', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('FG3M', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FG3A', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FG3_PCT', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('FTM', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FTA', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FT_PCT', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('TS_PCT', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('OREB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DREB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('TOV', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('PF', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['Player.player_id'], name='Season_player_id_fkey'),
    sa.PrimaryKeyConstraint('season_id', name='Season_pkey')
    )
    # ### end Alembic commands ###
