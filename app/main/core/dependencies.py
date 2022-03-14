from app.main.models import gestionnaire
from app.main.models.gestionnaire import Gestionnaire

from typing import Generator

from fastapi import Depends, HTTPException, status
import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.main import schemas,crud
from app.main.core import security
from app.main.core.config import Config
from app.main.models.database.session import SessionLocal


from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class TokenRequired(HTTPBearer):

    def __init__(self,  auto_error: bool = True):
        super(TokenRequired, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request, db: Session = Depends(get_db),):
        credentials: HTTPAuthorizationCredentials = await super(TokenRequired, self).__call__(request)
        
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Votre session est non valide.")
            
            token_data = self.verify_jwt(credentials.credentials)
            if not token_data:
                raise HTTPException(status_code=403, detail="Votre session est invalide ou expirée")
            
            gestionnaire_user = crud.gestionnaire.get_by_public_id(db=db, public_id=token_data.__sub__)
            gestionnaire_user = db.query(gestionnaire).filter_by(public_id=token_data.__sub__).first()
            if not gestionnaire_user:
                raise HTTPException(status_code=403, detail="Votre session est invalide ou expirée")
                
            return gestionnaire_user
        else:
            raise HTTPException(status_code=403, detail="Code d'autorisation non valide.")

    
    def verify_jwt(self, token: str) -> bool:

        isTokenValid: bool = False

        try:
            payload = jwt.decode(
                token, Config.SECRET_KEY, algorithms=[security.ALGORITHM]
            )
            token_data = schemas.TokenPayload(**payload)
            return token_data
        except (jwt.InvalidTokenError, ValidationError) as e:
            payload = None
            
        if payload:
            isTokenValid = True
        return isTokenValid