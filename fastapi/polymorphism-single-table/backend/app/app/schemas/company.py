from typing import Optional, List

from pydantic import BaseModel
from .employee.manager import Manager
from .employee.engineer import Engineer
# Shared properties
class CompanyBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on company creation
class CompanyCreate(CompanyBase):
    name: str


# Properties to receive on company update
class CompanyUpdate(CompanyBase):
    pass


# Properties shared by models stored in DB
class CompanyInDBBase(CompanyBase):
    id: int
    name: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Company(CompanyInDBBase):
    managers: Optional[List[Manager]]
    engineers: Optional[List[Engineer]]


# Properties properties stored in DB
class CompanyInDB(CompanyInDBBase):
    pass
