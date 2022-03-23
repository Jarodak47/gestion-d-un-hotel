from typing import List

from app.main import models
from ..models.stock import StockType
from pydantic import BaseModel
from .base import DataList

# Shared properties
class StockBase(BaseModel):
    type : models.StockType
    #fId : int
    #dId : int
    title : str
    price : float
    Qte : int
    

# Properties to receive via API on creation
class StockCreate(StockBase):
    pass

# Properties to receive via API on update
class StockUpdate(StockBase):
    id : int

# Properties to receive via API on deleting
class StockDelete(StockBase):
    id : int




# Additional Properties to store in db via API on creation
class StockInDBBase(StockBase):
    id: int
    class Config:
        orm_mode = True

class Stock(StockInDBBase):
    pass

class StockList(DataList):
    data: List[StockBase] = []
