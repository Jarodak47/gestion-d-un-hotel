from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer,Enum,types 
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


class ReservationState(str, Enum):
# une reservation a 03 etats : inactive,en cours(loading),en attente(awaiting)
    UNACTIVED ="UNACTIVED"
    LOADING = "LOADING"
    AWAITING = "AWAITING"


@dataclass    
class Reservation(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "reservation"

    rId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    chId = Column(Integer, ForeignKey('chambre.chId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    cId = Column(Integer, ForeignKey('client.cId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    rDate = Column (datetime.now,nullable=False,index=True)
    rState = Column(types.Enum(ReservationState),nullable=True,unique=True,default=ReservationState.AWAITING)
    chambrer = relationship("Chambre", foreign_keys=[chId], backref="reservation")
    clienter = relationship("Client", foreign_keys=[cId], backref="reservation")





    
    