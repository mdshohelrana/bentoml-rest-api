import pytest
from services.data_prediction_service import DataPredictionService

def test_get_predictions():
    service = DataPredictionService()
    predictions = service.get_predictions()
    assert isinstance(predictions, list)
    assert len(predictions) > 0
