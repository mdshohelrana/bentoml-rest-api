import typing as t
import numpy as np
import bentoml
from sklearn.metrics import mean_squared_error
from services.data_prediction_service import DataPredictionService


@bentoml.service()
class DataRMSEService:
    data_prediction_service = bentoml.depends(DataPredictionService)

    @bentoml.api()
    def get_rmse(self) -> float:
        y_test, y_pred = self.data_prediction_service.get_test_and_pred()
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        return rmse
