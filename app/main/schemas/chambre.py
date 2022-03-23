from pydantic import BaseModel
from app.main import models

# Shared properties
class ChambreBase(BaseModel):
    description : str
    price : int
    
# Properties to receive via API on creation
class ChambreCreate(ChambreBase):
    pass

# Properties to receive via API on update
class ChambreUpdate(ChambreBase):
    id : int

class ChambreDelete(ChambreBase):
    id : int
    
# Additional Properties to store in db via API on creation
class ChambreInDBBase(ChambreBase):
    id: int
    status:models.ChstatusType

    class Config:
        orm_mode = True

# Additional properties to return via API
class Chambre(ChambreInDBBase):
    pass

# Additional properties stored in DB
class ChambreInDB(ChambreInDBBase):
    pass
