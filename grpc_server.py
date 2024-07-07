from concurrent import futures
import grpc
from grpc import model_pb2_grpc, model_pb2
from services.data_broker_service import DataBrokerService
from services.data_prediction_service import DataPredictionService
from services.data_rmse_service import DataRMSEService


class FinancialModelServicer(model_pb2_grpc.FinancialModelServicer):
    def __init__(self):
        self.data_broker_service = DataBrokerService()
        self.data_prediction_service = DataPredictionService()
        self.data_rmse_service = DataRMSEService()

    def GetDataHead(self, request, context):
        data_head = self.data_broker_service.get_data_head()
        response = model_pb2.DataHeadResponse()
        for row in data_head:
            response.data_head.append(row)
        return response

    def GetPredictions(self, request, context):
        predictions = self.data_prediction_service.get_predictions()
        return model_pb2.PredictionsResponse(predictions=predictions)

    def GetRMSE(self, request, context):
        rmse = self.data_rmse_service.get_rmse()
        return model_pb2.RMSEResponse(rmse=rmse)

    def GetInference(self, request, context):
        data_head = self.data_broker_service.get_data_head()
        predictions = self.data_prediction_service.get_predictions()
        rmse = self.data_rmse_service.get_rmse()
        response = model_pb2.InferenceResponse(
            data_head=data_head,
            predictions=predictions,
            rmse=rmse
        )
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_FinancialModelServicer_to_server(
        FinancialModelServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
