from datetime import datetime
from typing import List, Optional
from fastapi import Body
from sqlalchemy import DateTime
from app.main import models
from pydantic import BaseModel, EmailStr


from .base import DataList



# Shared properties
class ReservationBase(BaseModel):
    beginDate :Optional[datetime]
    endDate : Optional[datetime]
    chaId : int
    clId : int
    total : int
    


# Properties to receive via API on creation
class ReservationCreate (ReservationBase):
    pass


# Properties to receive via API on update
class ReservationUpdate(ReservationBase):
    resId : int

class ReservationDelete(ReservationBase):
    resId : int



# Additional Properties to store in db via API on creation
class ReservationInDBBase(ReservationBase):
    state : models.ReservationState
    resId :int
    createdDate :Optional[datetime]=None
    class Config:
        orm_mode = True


# Additional properties to return via API
class Reservation(ReservationInDBBase):
    pass


class ReservationList(DataList):
    data: List[ReservationBase] = []

    
