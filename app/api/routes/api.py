from fastapi import APIRouter
from app.api.routes.exchange import api

router = APIRouter(prefix="/api")
router.include_router(api.router, prefix="/exchange")


