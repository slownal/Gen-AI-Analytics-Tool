from fastapi import APIRouter
from app.api.endpoints import query, explain, validate

api_router = APIRouter()

api_router.include_router(query.router, prefix="/query", tags=["query"])
api_router.include_router(explain.router, prefix="/explain", tags=["explain"])
api_router.include_router(validate.router, prefix="/validate", tags=["validate"]) 