import email

from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base


@dataclass    
class Gestionnaire(Base):

    """ modèle de données pour l'enregistrement des gestionnaires dans la base de données"""
    __tablename__ = "food"


    gPublicId = Column(String,nullable=False)
    gId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    name = Column(String,nullable=False)
    firstname = Column(String,nullable=False)
    eMail = Column(email,nullable=False)
    
