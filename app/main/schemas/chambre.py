from pydantic import BaseModel

# Shared properties
class ChambreBase(BaseModel):
    chDescription : str
    chPrice : float
    
# Properties to receive via API on creation
class ChambreCreate(ChambreBase):
    pass

# Properties to receive via API on update
class ChambreUpdate(ChambreBase):
    chId : int
    
# Additional Properties to store in db via API on creation
class ChambreInDBBase(ChambreBase):
    chId: int
    chStatus:str

    class Config:
        orm_mode = True

# Additional properties to return via API
class Chambre(ChambreInDBBase):
    pass

# Additional properties stored in DB
class ChambreInDB(ChambreInDBBase):
    pass
