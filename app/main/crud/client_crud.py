from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.models.client import Client
from app.main.schemas.client import  ClientCreate, ClientUpdate




class CRUDChambre(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def get_by_phoneNumber(self, db: Session, *, phoneNumber: str) -> Optional[Client]:
        return db.query(Client).filter(Client.phoneNumber == phoneNumber).first()
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Client]:
        return db.query(Client).filter(Client.id == id).first()

    def create(self, db: Session, *, obj_in: ClientCreate) -> Client:
        db_obj = Client(
            name =obj_in.name,
            firstname = obj_in.firstname,
            email = obj_in.email,
            phoneNumber = obj_in.phoneNumber
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Client, obj_in: Union[ClientUpdate, Dict[str, Any]]
    ) -> Client:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    def remove(self, db: Session, *, id: int) -> Client:
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
client = CRUDChambre(Client)