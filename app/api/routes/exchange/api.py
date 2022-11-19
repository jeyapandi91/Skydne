from fastapi import APIRouter, Depends
from app.api.routes.exchange import bittrex
from app.utils.dependency import authenticate

router = APIRouter()

router.include_router(bittrex.router, prefix="/bittrex", tags=["bittrex"], dependencies=[Depends(authenticate)])