from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
# you must import tables
from app.models.employee import Manager, Engineer
if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    managers = relationship("Manager", back_populates="company")
    engineers = relationship("Engineer", back_populates="company")
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="companys")
