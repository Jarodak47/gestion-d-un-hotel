from datetime import datetime
#from app.main.models.food import Food
#from app.main.models.drink import Drink
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


@dataclass    
class Commande(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "commande"
    title = Column(String)
    cmdId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    clId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False, index=True)  
    stockId = Column(Integer, ForeignKey('Stock.sId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False, index=True)
    date = Column (datetime.now,nullable=False,index=True)
    Qte = Column(Integer ,index=True, nullable=True, default=0)  
    stocker = relationship("Stock", foreign_keys=[stockId], backref="commande")
    clienter = relationship("Client", foreign_keys=[clId], backref="commande")





    
    