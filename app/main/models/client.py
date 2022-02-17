import email
from msilib import gen_uuid
from uuid import UUID


from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base


@dataclass    
class Client(Base):

    """ modèle de données pour l'enregistrement des clients dans la base de données"""
    __tablename__ = "client"


    publicId = Column(str(UUID),nullable=False)
    cId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    name = Column(String,nullable=False)
    firstname = Column(String,nullable=False)
    email = Column(email,nullable=False)
    phoneNumber =Column(Integer,nullable=True,index=True)
    
    
