from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.session import Base


class Chambre(Base):
    __tablename__ = "chambres"

    chId = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    chDescription = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")