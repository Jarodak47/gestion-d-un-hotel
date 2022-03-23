from app.main.models.food import Food
from app.main.models.drink import Drink
from sqlalchemy import  INTEGER, Boolean, Column, ForeignKey, Integer, String, Table,types,MetaData
from sqlalchemy.orm import relationship
from enum import Enum
from dataclasses import dataclass
from app.main.models.database.base_class import Base


class StockType(str, Enum):

    FOOD = "Food"
    DRINK = "Drink"

@dataclass    
class Stock(Base):

    """ modèle de données pour l'enregistrement des boissons dans la base de données"""
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    fId = Column(Integer, ForeignKey('recipees.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False,index=True)  
    dId = Column(Integer, ForeignKey('drink.id', ondelete="CASCADE",onupdate="CASCADE"), nullable=False,index=True)  
    #type = Column(types.Enum(StockType),index=True, nullable=False)
    title = Column(String,nullable=False)
    Qte = Column(Integer,default=0)
    #"min", "max", "opt", name="ValueTypes")
    #is_empty = Column(Boolean(), default=True)
    #status = Column(types.Enum(UserStatusType), index=True, nullable=False, default=UserStatusType.UNACTIVED)

    feeder = relationship("Food", foreign_keys=[fId], backref="stock")
    drinker = relationship("Drink", foreign_keys=[dId], backref="stock")





    
    