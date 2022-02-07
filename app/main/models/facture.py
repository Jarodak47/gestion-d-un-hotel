from app.main.models.food import Food
from app.main.models.drink import Drink
from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String,Enum, Table,types,MetaData
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


class ReservationState(str, Enum):
# une reservation a 03 etats : inactive,en cours(loading),en attente(awaiting)
    UNACTIVED ="UNACTIVED"
    LOADING = "LOADING"
    AWAITING = "AWAITING"


@dataclass    
class Facture(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "facture"

    faId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    gId = Column(Integer, ForeignKey('gestionnaire.chId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    cId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    rId = Column(Integer, ForeignKey('reservation.rId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)
    coId = Column(Integer, ForeignKey('commande.coId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    gestner = relationship("Gestionnaire", foreign_keys=[gId], backref="facture")
    clienter = relationship("Client", foreign_keys=[cId], backref="facture")
    reserver = relationship("Reservation", foreign_keys=[rId], backref="facture")
    commander = relationship("Commande", foreign_keys=[coId], backref="facture")







    
    