from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.core.security import get_password_hash,verify_password
from app.main.models.gestionnaire import Gestionnaire
from app.main.schemas.gestionnaire import  GestionnaireCreate, GestionnaireUpdate




class CRUDGestionnaire(CRUDBase[Gestionnaire, GestionnaireCreate, GestionnaireUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Gestionnaire]:
        return db.query(Gestionnaire).filter(Gestionnaire.email == email).first()
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Gestionnaire]:
        return db.query(Gestionnaire).filter(Gestionnaire.id == id).first()

    def create(self, db: Session, *, obj_in: GestionnaireCreate) -> Gestionnaire:
        db_obj = Gestionnaire(
            name =obj_in.name,
            firstname = obj_in.firstname,
            email=obj_in.email,
            phoneNumber=obj_in.phoneNumber,
            hashedPassword=get_password_hash(obj_in.password) 
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Gestionnaire, obj_in: Union[GestionnaireUpdate, Dict[str, Any]]
    ) -> Gestionnaire:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashedPassword = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashedPassword
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[Gestionnaire]:
        gestionnaire = self.get_by_email(db, email=email)
        if not gestionnaire:
            return None
        if not verify_password(password, gestionnaire.hashedPassword):
            return None
        return gestionnaire
    
    def remove(self, db: Session, *, id: int) -> Gestionnaire:
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
gestionnaire = CRUDGestionnaire(Gestionnaire)