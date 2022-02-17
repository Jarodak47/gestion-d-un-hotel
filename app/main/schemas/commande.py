from typing import List, Optional
from sqlalchemy import DateTime
from pydantic import BaseModel
from .base import DataList
import client,stock

# Shared properties
class CommandeBase(BaseModel):
    sType : str
    cTitle  : str
    name : str(client.ClientBase.name)
    firstname : str(client.ClientBase.firstname)
    email : str(client.ClientBase.email)
    phoneNumber : Optional[str](client.ClientBase.phoneNumber)
    cQte : int
    class Config:
        orm_mode = True

# Properties to receive via API on creation
class CommandeCreate (CommandeBase):
    pass

# Properties to receive via API on update
class CommandeUpdate(CommandeBase):
    coId : int

class CommandeDelete(CommandeBase):
    coId : int

# Additional Properties to store in db via API on creation
class CommandeInDBBase(CommandeBase):
    coId : int
    cId : int
    sId : int
    coDatetime :DateTime
    
    class Config:
        orm_mode = True

# Additional properties to return via API
class Commande(CommandeInDBBase):
    pass

class CommandeList(DataList):
    data: List[CommandeBase] = []

    
