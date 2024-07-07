import grpc
import model_pb2
import model_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = model_pb2_grpc.FinancialModelStub(channel)

        response = stub.GetDataHead(model_pb2.Empty())
        print("Data Head:", response.head)

        response = stub.Predict(model_pb2.Empty())
        print("MSE:", response.mse)
        print("Predictions:", response.predictions)


if __name__ == '__main__':
    run()
