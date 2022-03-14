import email
from uuid import UUID

from sqlalchemy import   Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from app.main.models.database.base_class import Base


@dataclass    
class Gestionnaire(Base):

    """ modèle de données pour l'enregistrement des gestionnaires dans la base de données"""
    __tablename__ = "food"


    publicId = Column(str(UUID),nullable=False)
    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    name = Column(String,nullable=False)
    firstname = Column(String,nullable=False)
    email = Column(str(email),nullable=False, unique=True)
    hashedPassword =Column(String,nullable=False,index=True)
    #is_active = Column(Boolean(), default=True)
    #is_superuser = Column(Boolean(), default=False)
    
