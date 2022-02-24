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

    resId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    chaId = Column(Integer, ForeignKey('chambre.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    clId = Column(Integer, ForeignKey('client.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    createdDate = Column (datetime.now,nullable=False,index=True)
    startDate = Column (datetime,nullable=False,index=True)
    endDate =  Column (datetime,nullable=False,index=True)
    state = Column(types.Enum(ReservationState),nullable=True,unique=True,default=ReservationState.AWAITING)
    chambrer = relationship("Chambre", foreign_keys=[chaId], backref="reservation")
    clienter = relationship("Client", foreign_keys=[clId], backref="reservation")





    
    