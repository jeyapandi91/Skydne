import pytest
from httpx import AsyncClient
import asyncio
import base64

from app.main import app
import os


@pytest.mark.asyncio
async def test_market_summaries_200_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        valid_credentials = base64.b64encode(b"skydne:password").decode("utf-8")
        response = await ac.get("/api/exchange/bittrex/",headers={"Authorization": "Basic " + valid_credentials})
    assert response.status_code == 200
    status = response.json()
    assert status["status"] == "OK"

@pytest.mark.asyncio
async def test_market_summaries_401_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        valid_credentials =  base64.b64encode(b"skydne:passwor").decode("utf-8")
        response = await ac.get("/api/exchange/bittrex/",headers={"Authorization": "Basic " + valid_credentials})
    assert response.status_code == 401
    status = response.json()
    assert status["detail"] == "Incorrect email or password"

@pytest.mark.asyncio
async def test_market_summaries_404_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        valid_credentials =  base64.b64encode(b"skydne:password").decode("utf-8")
        response = await ac.get("/api/exchange/bittrexx/",headers={"Authorization": "Basic " + valid_credentials})
    assert response.status_code == 404
    status = response.json()
    assert status["detail"] == "Not Found"
    

@pytest.mark.asyncio
async def test_market_symbol_200_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        valid_credentials = base64.b64encode(b"skydne:password").decode("utf-8")
        response = await ac.get("api/exchange/bittrex/ltc-btc",headers={"Authorization": "Basic " + valid_credentials})
    assert response.status_code == 200
    status = response.json()
    assert status["status"] == "OK"

@pytest.mark.asyncio
async def test_market_symbol_401_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        valid_credentials =  base64.b64encode(b"skydn:password").decode("utf-8")
        response = await ac.get("api/exchange/bittrex/ltc-btf",headers={"Authorization": "Basic " + valid_credentials})
    assert response.status_code == 401
    status = response.json()
    assert status["detail"] == "Incorrect email or password"

@pytest.mark.asyncio
async def test_market_symbol_404_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        valid_credentials =  base64.b64encode(b"skydne:password").decode("utf-8")
        response = await ac.get("api/exchange/bittrex/ltc-btf",headers={"Authorization": "Basic " + valid_credentials})
    status = response.json()
    assert status["status"] == "FAIL"


