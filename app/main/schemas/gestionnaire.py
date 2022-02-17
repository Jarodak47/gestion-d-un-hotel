from typing import Optional
from pydantic import BaseModel, EmailStr

# Shared properties
class GestionnaireBase(BaseModel):
    name : str
    firstname : str
    email : EmailStr
    phoneNumber : Optional[str]
    
# Properties to receive via API on creation
class GestionnaireCreate(GestionnaireBase):
    password: str

# Properties to receive via API on update
class GestionnaireUpdate(GestionnaireBase):
    gId : int
    password: Optional[str] = None
    
# Additional Properties to store in db via API on creation
class GestionnaireInDBBase(GestionnaireBase):
    gId: int
    gPublicId : str
    password: str

    class Config:
        orm_mode = True

# Additional properties to return via API
class Gestionnaire(GestionnaireInDBBase):
    pass

# Additional properties stored in DB
class GestionnaireInDB(GestionnaireInDBBase):
    pass
