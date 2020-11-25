from typing import Optional
from enum import Enum
from pydantic import BaseModel
# Employee Types
class EmployeeEnum(str, Enum):
    manager = 'manager'
    engineer = 'engineer'

# Shared properties
class EmployeeBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on employee creation
class EmployeeCreate(EmployeeBase):
    name: str
    employee_type: EmployeeEnum

# Properties to receive on employee update
class EmployeeUpdate(EmployeeBase):
    pass


# Properties shared by models stored in DB
class EmployeeInDBBase(EmployeeBase):
    id: int
    name: str
    employee_type: EmployeeEnum

    class Config:
        orm_mode = True


# Properties to return to client
class Employee(EmployeeInDBBase):
    pass


# Properties properties stored in DB
class EmployeeInDB(EmployeeInDBBase):
    pass
