from datetime import datetime
#from app.main.models.food import Food
#from app.main.models.drink import Drink
from sqlalchemy import  Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from app.main.models.database.base_class import Base

@dataclass    
class Commande(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "commande"
    title = Column(String)
    cmdId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    clId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False, index=True)  
    stockId = Column(Integer, ForeignKey('Stock.sId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False, index=True)
    createDate :any = Column(DateTime(), server_default=func.now(), onupdate=datetime.now())

    Qte = Column(Integer ,index=True, nullable=True, default=0)  
    stocker = relationship("Stock", foreign_keys=[stockId], backref="commande")
    clienter = relationship("Client", foreign_keys=[clId], backref="commande")





    
    