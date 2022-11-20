from fastapi import FastAPI
from app.api.routes import api
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(api.router)

@app.get("/health")
async def health():
    """health route"""
    return {"status": "UP"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Sky DNE – API ",
        version="1.0.0",
        description="Micro service app to fetch crypto currency market",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


