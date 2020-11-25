from typing import TYPE_CHECKING

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
import enum
if TYPE_CHECKING:
    from .user import User  # noqa: F401

class EmployeeEnum(str, enum.Enum):
    """class for validating employee types"""
    manager = "manager"
    engineer = "engineer"


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    employee_type = Column(Enum(EmployeeEnum))

    __mapper_args__ = {
        'polymorphic_identity':'employee',
        'polymorphic_on': employee_type
    }

class Manager(Employee):
    __tablename__ = 'manager'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    foo = Column(String(30))

    company_id = Column(ForeignKey('company.id'))
    company = relationship("Company", back_populates="managers")

    __mapper_args__ = {
        'polymorphic_identity':'manager',
    }

class Engineer(Employee):
    __tablename__ = 'engineer'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    bar = Column(String(30))

    company_id = Column(ForeignKey('company.id'))
    company = relationship("Company", back_populates="engineers")

    __mapper_args__ = {
        'polymorphic_identity':'engineer',
    }
