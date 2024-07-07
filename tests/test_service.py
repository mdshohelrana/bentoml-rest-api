import pytest
from service import InferenceGraphService

@pytest.mark.asyncio
async def test_get_inference():
    service = InferenceGraphService()
    result = await service.get_inference()
    assert "data_head" in result
    assert "predictions" in result
    assert "rmse" in result
