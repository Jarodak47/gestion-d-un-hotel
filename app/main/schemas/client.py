from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ClientBase(BaseModel):
    name : str
    firstname : str
    email : Optional[EmailStr]
    phoneNumber : Optional[str]

    #publicId = Column(str(UUID),nullable=False)
    #cId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    

# Properties to receive via API on creation
class ClientCreate(ClientBase):
    password: str


# Properties to receive via API on update
class ClientUpdate(ClientBase):
    password: Optional[str] = None
    cId : int

# Properties to store in db via api on creation
class ClientInDBBase(ClientBase):
    cId: int
    publicId : str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Client(ClientInDBBase):
    pass


# Additional properties stored in DB
class ClientInDB(ClientInDBBase):
    pass
