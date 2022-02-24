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

    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    description = Column(String, unique=False, index=True,nullable=True)
    price = Column(float,nullable=False)
    status = Column(types.Enum(ChstatusType), index=True, nullable=False, default=ChstatusType.OPENED)