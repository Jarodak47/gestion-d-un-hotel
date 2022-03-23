from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from app.main.models.database.base_class import Base



   

@dataclass    
class Drink(Base):

    """ modèle de données pour l'enregistrement des boissons dans la base de données"""
    __tablename__ = "drink"

    Id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    name = Column(String, unique=True, index=True,nullable=False)
    price = Column(INTEGER,nullable=False,index=True)
    Qte = Column(INTEGER ,index=True, nullable=True, default=0)
