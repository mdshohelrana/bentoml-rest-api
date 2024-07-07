import typing as t
import numpy as np
import bentoml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from common.utils import load_data


@bentoml.service()
class DataPredictionService:
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
    def get_test_and_pred(self) -> t.Tuple[t.List[float], t.List[float]]:
        return self.y_test.tolist(), self.y_pred.tolist()
