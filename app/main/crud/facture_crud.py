from turtle import title
from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.models.facture import Facture
from app.main.schemas.facture import  FactureCreate,FactureUpdate




class CRUDFacture(CRUDBase[Facture, FactureCreate, FactureUpdate]):
    def get_by_reservation_id(self, db: Session, *, id: int) -> Optional[Facture]:
        return db.query(Facture).filter(Facture.resId == id).first()

    def get_by_commande_id(self, db: Session, *, id: int) -> Optional[Facture]:
        return db.query(Facture).filter(Facture.cmdId == id).first()
    
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Facture]:
        return db.query(Facture).filter(Facture.faId == id).first()

    def create(self, db: Session, *, obj_in: FactureCreate) -> Facture:
        db_obj = Facture(
            title = obj_in.title,
            resId = obj_in.resId,
            cmdId = obj_in.cmdId,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Facture, obj_in: Union[FactureUpdate, Dict[str, Any]]
    ) -> Facture:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    def remove(self, db: Session, *, id: int) -> Facture:
        obj = db.query(self.get_by_id).get(id)
        db.delete(obj)
        db.commit()
        return obj
    '''
    #fonctionnality to add next time

    def is_active(self, gestionnaire: Gestionnaire) -> bool:
        return gestionnaire.is_active

    def is_superuser(self, gestionnaire: Gestionnaire) -> bool:
        return gestionnaire.is_superuser

    '''
facture = CRUDFacture(Facture)