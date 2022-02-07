from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base



   

@dataclass    
class Drink(Base):

    """ modèle de données pour l'enregistrement des boissons dans la base de données"""
    __tablename__ = "drink"

    dId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    dName = Column(String, unique=True, index=True,nullable=False)
    dPrice = Column(float,nullable=False,index=True)
    dQte = Column(INTEGER ,index=True, nullable=True, default=0)
