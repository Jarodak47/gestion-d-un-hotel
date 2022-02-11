from app.main.models.food import Food
from app.main.models.drink import Drink
from sqlalchemy import  INTEGER, Column, ForeignKey, Integer, String,Enum, Table,types,MetaData
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from database.session import Base


class stockType(str, Enum):

    FOOD = "Food"
    DRINK = "Drink"

@dataclass    
class Stock(Base):

    """ modèle de données pour l'enregistrement des boissons dans la base de données"""
    __tablename__ = "stock"

    sId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    fId = Column(Integer, ForeignKey('food.fId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False,index=True)  
    dId = Column(Integer, ForeignKey('drink.dId', ondelete="CASCADE",onupdate="CASCADE"), nullable=False,index=True)  
    sType = Column(types.Enum(stockType),nullable=True,unique=True)

    feeder = relationship("Food", foreign_keys=[fId], backref="stock")
    drinker = relationship("Drink", foreign_keys=[dId], backref="stock")





    
    