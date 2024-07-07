import pytest
from bentoml.testing.utils import async_client
from service import StockPredictionService


@pytest.mark.asyncio
async def test_end_to_end():
    service = StockPredictionService()

    async with async_client(service) as client:
        response = await client.async_request("GET", "/get_predictions")
        assert response.status_code == 200
        prediction_data = response.json()
        assert len(prediction_data) > 0

        response = await client.async_request("GET", "/get_mse")
        assert response.status_code == 200
        mse_data = response.json()
        assert mse_data[0] >= 0
