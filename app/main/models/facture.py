from datetime import datetime
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


@dataclass    
class Facture(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "facture"

    title = Column(String,nullable=False)
    faId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    geId = Column(Integer, ForeignKey('gestionnaire.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    #clId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    resId = Column(Integer, ForeignKey('reservation.resId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    cost = Column(Integer,nullable=False ,default=100)
    date = Column (datetime.now,nullable=False,index=True)
    cmdId = Column(Integer, ForeignKey('commande.cmdId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    gestner = relationship("Gestionnaire", foreign_keys=[geId], backref="facture")
    #clienter = relationship("Client", foreign_keys=[clId], backref="facture")
    reserver = relationship("Reservation", foreign_keys=[resId], backref="facture")
    commander = relationship("Commande", foreign_keys=[cmdId], backref="facture")







    
    