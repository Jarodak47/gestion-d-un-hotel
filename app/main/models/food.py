from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base


@dataclass    
class Food(Base):

    """ modèle de données pour l'enregistrement des plats de nourritures dans la base de données"""
    __tablename__ = "food"

    fId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    fName = Column(String, unique=True, index=True,nullable=False)
    fPrice = Column(float,nullable=False,index=True)
    fQte = Column(INTEGER ,index=True, nullable=True, default=0)

