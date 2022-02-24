from typing import List, Optional
from sqlalchemy import DateTime
from pydantic import BaseModel
from .base import DataList

# Shared properties
class FactureBase(BaseModel):
    title : str
    geId  : Optional[int]
    resId : Optional[int]
    cmdId : Optional[int]

# Properties to receive via API on creation
class FactureCreate (FactureBase):
    pass

# Properties to receive via API on update
class FactureUpdate(FactureBase):
    faId : int

class FactureDelete(FactureBase):
    faId : int

# Additional Properties to store in db via API on creation
class FactureInDBBase(FactureBase):
    faId : int 
    cost : int  
    createdDate : DateTime
    class Config:
        orm_mode = True

# Additional properties to return via API
class Facture(FactureInDBBase):
    pass

class FactureList(DataList):
    data: List[FactureBase] = []

    
