import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_success(client: AsyncClient) -> None:
    payload = {
        "name": "Test Business",
        "email": "test@example.com",
        "password": "StrongPassword123",
    }

    response = await client.post("/business/create", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data
