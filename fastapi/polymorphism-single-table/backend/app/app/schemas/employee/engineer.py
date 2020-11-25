from typing import Optional, List
from enum import Enum
from pydantic import BaseModel
from . import EmployeeBase, EmployeeEnum
# Engineer Types

# Shared properties
class EngineerBase(EmployeeBase):
    foo: Optional[str] = None


# Properties to receive on employee creation
class EngineerCreate(EngineerBase):
    foo: str
    employee_type: EmployeeEnum = EmployeeEnum.engineer

# Properties to receive on employee update
class EngineerUpdate(EngineerBase):
    pass


# Properties shared by models stored in DB
class EngineerInDBBase(EngineerBase):
    id: int
    foo: str
    employee_type: EmployeeEnum = EmployeeEnum.engineer

    class Config:
        orm_mode = True


# Properties to return to client
class Engineer(EngineerInDBBase):
    pass


# Properties properties stored in DB
class EngineerInDB(EngineerInDBBase):
    pass
