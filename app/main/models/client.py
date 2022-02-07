import email
from unicodedata import numeric

from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base


@dataclass    
class Client(Base):

    """ modèle de données pour l'enregistrement des clients dans la base de données"""
    __tablename__ = "client"


    publicId = Column(String,nullable=False)
    cId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    name = Column(String,nullable=False)
    firstname = Column(String,nullable=False)
    eMail = Column(email,nullable=False)
    
    
