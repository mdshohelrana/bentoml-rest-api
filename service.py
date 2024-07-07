import typing as t
import bentoml
from services.data_broker_service import DataBrokerService
from services.data_prediction_service import DataPredictionService
from services.data_rmse_service import DataRMSEService


@bentoml.service()
class Svc:
    data_broker_service = bentoml.depends(DataBrokerService)
    data_prediction_service = bentoml.depends(DataPredictionService)
    data_rmse_service = bentoml.depends(DataRMSEService)

    @bentoml.api()
    async def get_data_head(self) -> t.List[t.Dict[str, t.Any]]:
        return self.data_broker_service.get_data_head()

    @bentoml.api()
    async def get_predictions(self) -> t.List[float]:
        return self.data_prediction_service.get_predictions()

    @bentoml.api()
    async def get_rmse(self) -> float:
        return self.data_rmse_service.get_rmse()

    @bentoml.api()
    async def get_inference(self) -> t.Dict[str, t.Any]:
        data_head = self.data_broker_service.get_data_head()
        predictions = self.data_prediction_service.get_predictions()
        rmse = self.data_rmse_service.get_rmse()

        return {
            "data_head": data_head,
            "predictions": predictions,
            "rmse": rmse
        }


svc = Svc()
