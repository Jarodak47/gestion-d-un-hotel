from typing import List
from ..models.stock import StockType
from pydantic import BaseModel
from .base import DataList

# Shared properties
class StockBase(BaseModel):
    sType : str(StockType)
    fId : int
    dId : int
    sName : str
    sPrice : float
    sQte : int
    class Config:
        orm_mode = True

# Properties to receive via API on creation
class StockCreate(StockBase):
    pass

# Properties to receive via API on update
class StockUpdate(StockBase):
    sId : int

# Properties to receive via API on deleting
class StockDelete(StockBase):
    sId : int

# Additional Properties to store in db via API on creation
class StocInDBBase(StockBase):
    sId: int
    class Config:
        orm_mode = True

class StockList(DataList):
    data: List[StockBase] = []
