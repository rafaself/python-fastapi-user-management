from sqlalchemy import Table, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from src.database.base import Base
from src.apps.permissions.models import permission_association, permissions_group_user_association


class PermissionGroup(Base):
    __tablename__ = "permissions_groups"

    id = Column(Integer, primary_key=True, index=True,
                nullable=False, autoincrement=True)
    name = Column(String, index=True, nullable=False)

    permissions = relationship(
        "Permission", secondary=permission_association, back_populates="permissions_group")
    users = relationship(
        "User", secondary=permissions_group_user_association, back_populates="permissions_group")

    __table_args__ = (
        UniqueConstraint("name", name="uq_name"),
    )
