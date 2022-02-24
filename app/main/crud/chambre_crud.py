from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.models.chambre import Chambre
from app.main.schemas.chambre import  ChambreCreate, ChambreUpdate




class CRUDChambre(CRUDBase[Chambre, ChambreCreate, ChambreUpdate]):
    def get_by_status(self, db: Session, *, status: str) -> Optional[Chambre]:
        return db.query(Chambre).filter(Chambre.status == status).first()
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Chambre]:
        return db.query(Chambre).filter(Chambre.id == id).first()

    def create(self, db: Session, *, obj_in: ChambreCreate) -> Chambre:
        db_obj = Chambre(
            description =obj_in.description,
            price = obj_in.price,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Chambre, obj_in: Union[ChambreUpdate, Dict[str, Any]]
    ) -> Chambre:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    def remove(self, db: Session, *, id: int) -> Chambre:
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
chambre = CRUDChambre(Chambre)