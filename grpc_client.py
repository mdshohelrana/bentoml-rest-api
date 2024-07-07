import grpc
from grpc import model_pb2_grpc, model_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = model_pb2_grpc.FinancialModelStub(channel)

        response = stub.GetDataHead(model_pb2.Empty())
        print("Data Head:", response.data_head)

        response = stub.GetPredictions(model_pb2.Empty())
        print("Predictions:", response.predictions)

        response = stub.GetRMSE(model_pb2.Empty())
        print("RMSE:", response.rmse)

        response = stub.GetInference(model_pb2.Empty())
        print("Inference - Data Head:", response.data_head)
        print("Inference - Predictions:", response.predictions)
        print("Inference - RMSE:", response.rmse)


if __name__ == '__main__':
    run()
