from pydantic import BaseModel


# Shared properties
class FoodBase(BaseModel):
    fName : str
    fPrice : float
    fQte : int
    

# Properties to receive via API on creation
class FoodCreate(FoodBase):
    pass


# Properties to receive via API on update
class FoodUpdate(FoodBase):
    fId : int
    
    

# Additional Properties to store in db via API on creation
class FoodInDBBase(FoodBase):
    fId: int
    
    class Config:
        orm_mode = True


# Additional properties to return via API
class Food(FoodInDBBase):
    pass


# Additional properties stored in DB
class FoodInDB(FoodInDBBase):
    pass
