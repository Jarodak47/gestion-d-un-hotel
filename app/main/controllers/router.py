from fastapi import APIRouter

from .gestionnaire_controller import router as gestionnaire

api_router = APIRouter()
api_router.include_router(gestionnaire)
