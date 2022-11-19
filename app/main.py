from fastapi import FastAPI
from app.api.routes import api

app = FastAPI()

app.include_router(api.router)

@app.get("/")
async def root():
    """skydne - python api root path"""
    return {"message": "Sky DNE – Python API Technical Exercise"}

@app.route("/health")
async def health():
    """health route"""
    return {"status": "UP"}
