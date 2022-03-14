from fastapi import HTTPException, APIRouter, Depends
from typing import List, Any
from fastapi.encoders import jsonable_encoder
from starlette.types import Message
from app.main.core import dependencies
from app.main import models, schemas,crud
from app.main.core.config import Config
from app.main.models.database import session

router = APIRouter(
    prefix="/gestionnaire",
    tags=["gestionnaire"],
    responses={
      404: {
        "description": "Not found"
      }
    },
  )

@router.post(" ", response_model=schemas.Gestionnaire)
def create_user(
    *,
    db: session = Depends(dependencies.get_db),
    gestionnaire_in: schemas.GestionnaireCreate,
    # current_user: models.User = Depends(dependencies.TokenRequired(roles=["Administrator"])),
) -> Any:
    """
    Create new user.
    """
    gestionnaire = crud.gestionnaire.get_by_email(db, email=gestionnaire_in.email)
    if gestionnaire:
        raise HTTPException(
            status_code=409,
            detail="This email already exists in the system.",
        )
    gestionnaire = crud.gestionnaire.create(db, obj_in=gestionnaire_in)
    #user = crud.user.update(db, db_obj=user, obj_in={
            # "status": models.UserStatusType.ACTIVED,
           # "role_id": 2})

    return gestionnaire
