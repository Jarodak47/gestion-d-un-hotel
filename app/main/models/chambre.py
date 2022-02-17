from sqlalchemy import  Column, ForeignKey, Integer, String,Enum,types
from sqlalchemy.orm import relationship

from dataclasses import dataclass
from database.session import Base

class ChstatusType(str, Enum):
# une chambre possède deux statuts : Ouvert et fermé.
    OPENED = "OPENED"
    CLOSED = "CLOSED"

@dataclass    
class Chambre(Base):

    """ modèle de données pour l'enregistrement des chambres dans la base de données"""
    __tablename__ = "chambre"

    chId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    chDescription = Column(String, unique=False, index=True,nullable=True)
    chPrice = Column(float,nullable=False)
    chStatus = Column(types.Enum(ChstatusType), index=True, nullable=False, default=ChstatusType.OPENED)