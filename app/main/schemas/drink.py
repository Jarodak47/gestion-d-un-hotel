from pydantic import BaseModel


# Shared properties
class DrinkBase(BaseModel):
    dName : str
    dPrice : float
    dQte : int
    

# Properties to receive via API on creation
class DrinkCreate(DrinkBase):
    pass


# Properties to receive via API on update
class DrinkUpdate(DrinkBase):
    dId : int
    
    

# Additional Properties to store in db via API on creation
class DrinkInDBBase(DrinkBase):
    dId: int
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class Drink(DrinkInDBBase):
    pass


# Additional properties stored in DB
class DrinkInDB(DrinkInDBBase):
    pass
