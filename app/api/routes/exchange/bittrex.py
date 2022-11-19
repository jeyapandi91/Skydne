from fastapi import APIRouter, HTTPException, Depends
from app.core.bittrex import Bittrex

router = APIRouter()

@router.get("/")
async def get_market_summaries():
    bittrex = Bittrex()
    return bittrex.get_market_summaries()

@router.get("/{symbol}")
async def get_market_summary(symbol: str):
    bittrex = Bittrex()
    return bittrex.get_market_summary(symbol)    


