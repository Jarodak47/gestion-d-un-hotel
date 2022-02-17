from datetime import datetime
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


@dataclass    
class Facture(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "facture"

    faTitle = Column(String,nullable=False)
    faId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    gId = Column(Integer, ForeignKey('gestionnaire.chId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    cId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    rId = Column(Integer, ForeignKey('reservation.rId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    tPrice = Column(Integer,nullable=False ,default=100)
    faDate = Column (datetime.now,nullable=False,index=True)
    coId = Column(Integer, ForeignKey('commande.coId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    gestner = relationship("Gestionnaire", foreign_keys=[gId], backref="facture")
    clienter = relationship("Client", foreign_keys=[cId], backref="facture")
    reserver = relationship("Reservation", foreign_keys=[rId], backref="facture")
    commander = relationship("Commande", foreign_keys=[coId], backref="facture")







    
    