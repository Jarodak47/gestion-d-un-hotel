from typing import List, Optional
from sqlalchemy import DateTime

from pydantic import BaseModel, EmailStr
from .base import DataList



# Shared properties
class ReservationBase(BaseModel):
    rDate : DateTime
    chDescription : str
    name : str
    firstname : str
    email : EmailStr
    phoneNumber : Optional[str]
    total : int
    class Config:
        orm_mode = True


# Properties to receive via API on creation
class ReservationCreate (ReservationBase):
    pass


# Properties to receive via API on update
class ReservationUpdate(ReservationBase):
    rId : int

class ReservationDelete(ReservationBase):
    rId : int



# Additional Properties to store in db via API on creation
class ReservationInDBBase(ReservationBase):
    rState : str
    rDatetime :DateTime
    class Config:
        orm_mode = True


# Additional properties to return via API
class Reservation(ReservationInDBBase):
    pass


class ReservationList(DataList):
    data: List[ReservationBase] = []

    
