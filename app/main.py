from fastapi import FastAPI
from app.api.routes import api


app = FastAPI()

app.include_router(api.router)

@app.get("/health")
async def health():
    """health route"""
    return {"status": "UP"}




