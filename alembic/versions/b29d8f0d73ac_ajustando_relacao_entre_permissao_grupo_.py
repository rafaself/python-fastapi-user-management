"""ajustando relacao entre permissao, grupo e usuario para serem unicas

Revision ID: b29d8f0d73ac
Revises: 8b2f86db2e56
Create Date: 2024-01-12 17:48:04.822207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b29d8f0d73ac'
down_revision = '8b2f86db2e56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_permission_association', 'permission_association', [
                                'permission_id', 'permission_group_id'])
    op.create_unique_constraint('uq_permissions_group_user_association',
                                'permissions_group_user_association', ['user_id', 'permission_group_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_permissions_group_user_association',
                       'permissions_group_user_association', type_='unique')
    op.drop_constraint('uq_permission_association',
                       'permission_association', type_='unique')
    # ### end Alembic commands ###
