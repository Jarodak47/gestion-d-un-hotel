from datetime import datetime
from enum import Enum
from sqlalchemy import Column, DateTime, ForeignKey, Integer,types 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from app.main.models.database.base_class import Base


class ReservationState(str, Enum):
# une reservation a 03 etats : inactive,en cours(loading),en attente(awaiting)
    UNACTIVED ="UNACTIVED"
    LOADING = "LOADING"
    AWAITING = "AWAITING"


@dataclass    
class Reservation(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "reservation"

    resId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    chaId = Column(Integer, ForeignKey('chambre.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    clId = Column(Integer, ForeignKey('client.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    createdDate = Column(DateTime(), server_default=func.now(), onupdate=datetime.now())
    startDate :any = Column(DateTime(), server_default=func.now(), onupdate=datetime.now())
    endDate :any = Column(DateTime(), server_default=func.now(), onupdate=datetime.now())
    state = Column(types.Enum(ReservationState), index=True, nullable=False, default=ReservationState.UNACTIVED)    
    chambrer = relationship("Chambre", foreign_keys=[chaId], backref="reservation")
    clienter = relationship("Client", foreign_keys=[clId], backref="reservation")





    
    