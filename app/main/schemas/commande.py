from typing import List
from sqlalchemy import DateTime
from pydantic import BaseModel
from .base import DataList

# Shared properties
class CommandeBase(BaseModel):
    title  : str
    Qte : int
    clId : int
    stockId : int

# Properties to receive via API on creation
class CommandeCreate (CommandeBase):
    pass

# Properties to receive via API on update
class CommandeUpdate(CommandeBase):
    cmdId : int

class CommandeDelete(CommandeBase):
    cmdId : int

# Additional Properties to store in db via API on creation
class CommandeInDBBase(CommandeBase):
    cmdId : int
    date :DateTime
    
    class Config:
        orm_mode = True

# Additional properties to return via API
class Commande(CommandeInDBBase):
    pass

class CommandeList(DataList):
    data: List[CommandeBase] = []

    
