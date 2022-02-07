from app.main.models.food import Food
from app.main.models.drink import Drink
from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String,Enum, Table,types,MetaData
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


@dataclass    
class Commande(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "commande"

    coId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    cId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    sId = Column(Integer, ForeignKey('Stock.sId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    coQte = Column(INTEGER ,index=True, nullable=True, default=0)  
    stocker = relationship("Stock", foreign_keys=[sId], backref="commande")
    clienter = relationship("Client", foreign_keys=[cId], backref="commande")





    
    