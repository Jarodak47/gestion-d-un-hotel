from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import  Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from app.main.models.database.base_class import Base



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
    createDate :any = Column(DateTime(), server_default=func.now(), onupdate=datetime.now())
    cmdId = Column(Integer, ForeignKey('commande.cmdId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    gestner = relationship("Gestionnaire", foreign_keys=[geId], backref="facture")
    #clienter = relationship("Client", foreign_keys=[clId], backref="facture")
    reserver = relationship("Reservation", foreign_keys=[resId], backref="facture")
    commander = relationship("Commande", foreign_keys=[cmdId], backref="facture")







    
    