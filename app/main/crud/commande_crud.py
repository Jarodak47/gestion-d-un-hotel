from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.models.commande import Commande
from app.main.schemas.commande import  CommandeCreate, CommandeUpdate




class CRUDCommande(CRUDBase[Commande, CommandeCreate, CommandeUpdate]):
    def get_by_quantity(self, db: Session, *, Qte: int) -> Optional[Commande]:
        return db.query(Commande).filter(Commande.Qte == Qte).first()

    def get_by_client_id(self, db: Session, *, id: int) -> Optional[Commande]:
        return db.query(Commande).filter(Commande.clId == id).first()
    
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Commande]:
        return db.query(Commande).filter(Commande.cmdId == id).first()

    def create(self, db: Session, *, obj_in: CommandeCreate) -> Commande:
        db_obj = Commande(
            title =obj_in.title,
            Qte = obj_in.Qte,
            clId = obj_in.clId,
            stockId = obj_in.stockId,
            
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Commande, obj_in: Union[CommandeUpdate, Dict[str, Any]]
    ) -> Commande:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    def remove(self, db: Session, *, id: int) -> Commande:
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
commande = CRUDCommande(Commande)