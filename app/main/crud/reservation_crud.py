from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.models.reservation import Reservation
from app.main.schemas.reservation import  ReservationCreate, ReservationUpdate




class CRUDReservation(CRUDBase[Reservation, ReservationCreate, ReservationUpdate]):
    def get_by_chambre_id(self, db: Session, *, chaId: int) -> Optional[Reservation]:
        return db.query(Reservation).filter(Reservation.chaId == chaId).first()

    def get_by_client_id(self, db: Session, *, id: int) -> Optional[Reservation]:
        return db.query(Reservation).filter(Reservation.clId == id).first()
    
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Reservation]:
        return db.query(Reservation).filter(Reservation.resId == id).first()

    def create(self, db: Session, *, obj_in: ReservationCreate) -> Reservation:
        db_obj = Reservation(
            clId =obj_in.clId,
            chaId = obj_in.chaId,
            begin = obj_in.beginDate,
            end = obj_in.endDate,
            
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Reservation, obj_in: Union[ReservationUpdate, Dict[str, Any]]
    ) -> Reservation:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    def remove(self, db: Session, *, id: int) -> Reservation:
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
reservation = CRUDReservation(Reservation)