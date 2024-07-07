import pytest
from service import StockPredictionService


def test_get_predictions():
    service = StockPredictionService()
    predictions = service.get_predictions(None)
    assert predictions is not None
    assert len(predictions) > 0


def test_get_mse():
    service = StockPredictionService()
    mse = service.get_mse()
    assert mse is not None
    assert mse[0] >= 0
