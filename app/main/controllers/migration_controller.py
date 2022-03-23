import os
import sys
import shutil
from sqlalchemy.orm import Session
from sqlalchemy import Column, String
from dataclasses import dataclass
from datetime import timedelta
import json
from typing import Any
from alembic import context
from sqlalchemy.exc import (DatabaseError, IntegrityError)
import os 
import logging
from fastapi import APIRouter, Body, Depends, HTTPException
from app.main import crud, models, schemas
from app.main.core import dependencies
from app.main.core.security import get_password_hash, verify_password

# from app.main.models.db.base import Base
from app.main.core.config import Config
from app.main.models.db.session import engine
from app.main.models.db.base_class import Base
import platform

# target_metadata = Base.metadata

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/migration",
    tags=["migration"]
)

def check_user_access_key(admin_key: schemas.AdminKey):
    logger.info(f"Check user access key: {admin_key.key}")
    if admin_key.key not in [Config.ADMIN_KEY]:
        raise HTTPException(status_code=400, detail="Clé d'accès incorrecte")

@router.post("/create-database-tables", response_model=schemas.Msg, status_code=201)
async def create_database_tables(
    db: Session = Depends(dependencies.get_db),
    admin_key: schemas.AdminKey = Body(...)
) -> Any:
    """
    Create database structure (tables)
    """
    check_user_access_key(admin_key)
    """ Try to remove previous alembic tags in database """
    try:
        @dataclass
        class AlembicVersion(Base):
            __tablename__ = "alembic_version"
            version_num: str = Column(String(32), primary_key=True, unique=True)
        db.query(AlembicVersion).delete()
        db.commit()
    except Exception as e:
        pass

    """ Try to remove previous alembic versions folder """
    migrations_folder =  os.path.join(os.getcwd(), "alembic/versions")
    try:
        shutil.rmtree(migrations_folder)
    except Exception as e:
        pass
    """ create alembic versions folder content """
    try:
        os.mkdir(migrations_folder)
    except OSError:
        logger.info("Creation of the directory %s failed" % migrations_folder)
    else:
        logger.info("Successfully created the directory %s " % migrations_folder)

    try:
        if platform.system():
            os.system('set PYTHONPATH=. && alembic revision --autogenerate')
            os.system('set PYTHONPATH=. && alembic upgrade head')
        else:
            os.system('PYTHONPATH=. alembic revision --autogenerate')
            os.system('PYTHONPATH=. alembic upgrade head')
        """ Try to remove previous alembic versions folder """
        migrations_folder =  os.path.join(os.getcwd(), "alembic/versions")
        try:
            shutil.rmtree(migrations_folder)
        except Exception as e:
            pass

        return {"message": "Les tables de base de données ont été créées avec succès"}
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-user-roles", response_model=schemas.Msg, status_code=201)
async def create_user_roles(
    db: Session = Depends(dependencies.get_db),
    admin_key: schemas.AdminKey = Body(...)
) -> Any:
    """
    Create default user roles
    """
    check_user_access_key(admin_key)
    try:
        with open('{}/app/main/templates/default_data/roles.json'.format(os.getcwd())) as f:
            datas = json.load(f)
            for data in datas:
                user_role = crud.role.get_role_id(db, role_id=data["id"])
                if user_role:
                    user_role = crud.role.update(db, db_obj=user_role, obj_in=schemas.RoleUpdate(
                        title_en = data["title_en"],
                        title_fr = data["title_fr"]
                    ))
                else:
                    user_role = crud.role.create(db, obj_in=schemas.RoleCreate(
                        id = data["id"],
                        title_en = data["title_en"],
                        title_fr = data["title_fr"]
                    ))
        return {"message": "Les roles d'utilisateur par défaut ont été crée avec succès."}
    except IntegrityError as e:
        logger.error(str(e))
        raise HTTPException(status_code=409, detail="Les roles d'utilisateur par défaut existe déjà")
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Erreur du serveur")


@router.post("/create-admin-user", response_model=schemas.Msg, status_code=201)
async def create_admin_user(
    db: Session = Depends(dependencies.get_db),
    admin_key: schemas.AdminKey = Body(...)
) -> Any:
    """
    Create first admin user
    """
    check_user_access_key(admin_key)
    user = crud.user.get_by_email(db, email=Config.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=Config.FIRST_SUPERUSER,
            password=Config.FIRST_SUPERUSER_PASSWORD,
            firstname= Config.FIRST_SUPERUSER_FIRST_NAME,
            lastname=Config.FIRST_SUPERUSER_LASTNAME
        )
        user = crud.user.create(db, obj_in=user_in)
        user = crud.user.update(db, db_obj=user, obj_in={
            "status": models.UserStatusType.ACTIVED,
            "role_id": 1
        })
    return {"message": "Compte administrateur créé avec succès"}


# @router.post("/create-admin-user", response_model=schemas.Msg, status_code=201)
# async def create_admin_user(
#     db: Session = Depends(dependencies.get_db),
#     admin_key: schemas.AdminKey = Body(...)
# ) -> Any:
#     """
#     Create first admin user
#     """
#     check_user_access_key(admin_key)
#     user = crud.user.get_by_email(db, email=Config.FIRST_SUPERUSER)
#     if not user:
#         user_in = schemas.UserCreate(
#             email=Config.FIRST_SUPERUSER,
#             password=Config.FIRST_SUPERUSER_PASSWORD,
#             firstname= Config.FIRST_SUPERUSER_FIRST_NAME,
#             lastname=Config.FIRST_SUPERUSER_LASTNAME
#         )
#         user = crud.user.create(db, obj_in=user_in)
#         user = crud.user.update(db, db_obj=user, obj_in={
#             "status": models.UserStatusType.ACTIVED,
#             "role_id": 1
#         })
#     return {"message": "Compte administrateur créé avec succès"}
