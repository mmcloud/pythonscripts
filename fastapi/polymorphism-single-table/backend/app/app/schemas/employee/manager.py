from typing import Optional, List
from enum import Enum
from pydantic import BaseModel
from . import EmployeeBase, EmployeeEnum
# Manager Types

# Shared properties
class ManagerBase(EmployeeBase):
    bar: Optional[str] = None


# Properties to receive on employee creation
class ManagerCreate(ManagerBase):
    bar: str
    employee_type: EmployeeEnum = EmployeeEnum.manager

# Properties to receive on employee update
class ManagerUpdate(ManagerBase):
    pass


# Properties shared by models stored in DB
class ManagerInDBBase(ManagerBase):
    id: int
    bar: str
    employee_type: EmployeeEnum = EmployeeEnum.manager

    class Config:
        orm_mode = True


# Properties to return to client
class Manager(ManagerInDBBase):
    pass


# Properties properties stored in DB
class ManagerInDB(ManagerInDBBase):
    pass
