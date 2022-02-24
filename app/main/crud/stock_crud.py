from turtle import title
from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main.core.security import get_password_hash,verify_password
from app.main.models.stock import Stock
from app.main.schemas.stock import  StockCreate, StockUpdate




class CRUDStock(CRUDBase[Stock, StockCreate, StockUpdate]):
    def get_by_quantity(self, db: Session, *, Qte: str) -> Optional[Stock]:
        return db.query(Stock).filter(Stock.Qte == Qte).first()
    
    def get_by_id(self, db: Session, *, id: str) -> Optional[Stock]:
        return db.query(Stock).filter(Stock.id == id).first()

    def get_by_type(self, db: Session, *, type: str) -> Optional[Stock]:
        return db.query(Stock).filter(Stock.type == type).first()

    def create(self, db: Session, *, obj_in: StockCreate) -> Stock:
        db_obj = Stock(
            type = obj_in.type,
            title = obj_in.title,
            price = obj_in.price,
            Qte=obj_in.Qte,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Stock, obj_in: Union[StockUpdate, Dict[str, Any]]
    ) -> Stock:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    
    def remove(self, db: Session, *, id: int) -> Stock:
        obj = db.query(self.get_by_id).get(id)
        db.delete(obj)
        db.commit()
        return obj

    
    
    '''
    #fonctionnality to add next time
    def is_empty(self, stock: Stock) -> bool:
        return stock.is_empty

    def is_superuser(self, gestionnaire: Gestionnaire) -> bool:
        return gestionnaire.is_superuser

    '''
stock = CRUDStock(Stock)