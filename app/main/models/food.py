from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base


@dataclass    
class Food(Base):

    """ modèle de données pour l'enregistrement des plats de nourritures dans la base de données"""
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    name = Column(String, unique=True,nullable=False)
    price = Column(float,nullable=False,index=True)
    Qte = Column(INTEGER , nullable=True, default=0)

