from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc
from common.utils import get_data_head, predict_stock_prices


class FinancialModelServicer(model_pb2_grpc.FinancialModelServicer):
    def GetDataHead(self, request, context):
        head = get_data_head().to_dict()
        return model_pb2.DataHead(head=head)

    def Predict(self, request, context):
        mse, predictions = predict_stock_prices()
        return model_pb2.PredictionResponse(mse=mse, predictions=predictions)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_FinancialModelServicer_to_server(
        FinancialModelServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
