from fastapi import APIRouter
from api.similarity_routes import similarity_router
from api.explanation_routes import explanation_router

router = APIRouter()

router.include_router(similarity_router)
router.include_router(explanation_router)