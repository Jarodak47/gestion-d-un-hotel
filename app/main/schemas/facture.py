from typing import List
from sqlalchemy import DateTime
from pydantic import BaseModel
from .base import DataList

# Shared properties
class ReservationBase(BaseModel):
    faTitle: str
    class Config:
        orm_mode = True

# Properties to receive via API on creation
class ReservationCreate (ReservationBase):
    pass

# Properties to receive via API on update
class ReservationUpdate(ReservationBase):
    faId : int

class ReservationDelete(ReservationBase):
    faId : int

# Additional Properties to store in db via API on creation
class ReservationInDBBase(ReservationBase):
    faId : int 
    gId : int
    cId : int
    rId : int
    tPrice : int  
    coId : int
    faDatetime : DateTime
    class Config:
        orm_mode = True

# Additional properties to return via API
class Reservation(ReservationInDBBase):
    pass

class ReservationList(DataList):
    data: List[ReservationBase] = []

    
