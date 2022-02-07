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
class Reservation(Base):

    """ modèle de données pour les réservations  dans la base de données"""
    __tablename__ = "reservation"

    rId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    fId = Column(Integer, ForeignKey('food.fId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    dId = Column(Integer, ForeignKey('drink.dId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False)  
    sType = Column(types.Enum(stockType),nullable=True,unique=True)

    feeder = relationship("Food", foreign_keys=[fId], backref="stock")
    drinker = relationship("Drink", foreign_keys=[dId], backref="stock")





    
    