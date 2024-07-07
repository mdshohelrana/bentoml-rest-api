import typing as t
import numpy as np
import pandas as pd
import bentoml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from common.utils import get_data_head, load_data


@bentoml.service()
class DataHeadService:
    def __init__(self):
        self.data_head = get_data_head()

    @bentoml.api()
    def get_data_head(self) -> t.List[t.Dict[str, t.Any]]:
        return self.data_head.to_dict(orient='records')


@bentoml.service()
class StockPredictionService:
    def __init__(self):
        self.data = load_data()
        self.model = LinearRegression()
        self.train_model()

    def train_model(self):
        self.data['Previous_Close'] = self.data['Close'].shift(1)
        self.data = self.data.dropna()
        X = self.data[['Previous_Close']]
        y = self.data['Close']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, shuffle=False)
        self.model.fit(X_train, y_train)
        self.X_test, self.y_test = X_test, y_test
        self.y_pred = self.model.predict(X_test)
        self.rmse = np.sqrt(mean_squared_error(y_test, self.y_pred))

    @bentoml.api()
    def get_predictions(self) -> t.List[float]:
        return self.y_pred.tolist()

    @bentoml.api()
    def get_rmse(self) -> float:
        return self.rmse


@bentoml.service()
class PredictionsService:
    stock_prediction_service = bentoml.depends(StockPredictionService)

    @bentoml.api()
    async def get_predictions(self) -> t.List[float]:
        return self.stock_prediction_service.get_predictions()


@bentoml.service()
class RMSEService:
    stock_prediction_service = bentoml.depends(StockPredictionService)

    @bentoml.api()
    async def get_rmse(self) -> float:
        return self.stock_prediction_service.get_rmse()


@bentoml.service()
class InferenceGraph:
    data_head_service = bentoml.depends(DataHeadService)
    stock_prediction_service = bentoml.depends(StockPredictionService)

    @bentoml.api()
    async def get_data_head(self) -> t.List[t.Dict[str, t.Any]]:
        return self.data_head_service.get_data_head()

    @bentoml.api()
    async def get_predictions(self) -> t.List[float]:
        return self.stock_prediction_service.get_predictions()

    @bentoml.api()
    async def get_rmse(self) -> float:
        return self.stock_prediction_service.get_rmse()

    @bentoml.api()
    async def get_inference(self) -> t.Dict[str, t.Any]:
        data_head = self.data_head_service.get_data_head()
        predictions = self.stock_prediction_service.get_predictions()
        rmse = self.stock_prediction_service.get_rmse()
        return {
            "data_head": data_head,
            "predictions": predictions,
            "rmse": rmse
        }


svc = InferenceGraph()
