import grpc
import bentoml_service_pb2
import bentoml_service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bentoml_service_pb2_grpc.BentoMLServiceStub(channel)

        # Get Data Head
        response = stub.GetDataHead(bentoml_service_pb2.Empty())
        print("Data Head:")
        for row in response.data_head:
            print(row.row)

        # Get Predictions
        response = stub.GetPredictions(bentoml_service_pb2.Empty())
        print("Predictions:", response.predictions)

        # Get RMSE
        response = stub.GetRMSE(bentoml_service_pb2.Empty())
        print("RMSE:", response.rmse)

        # Get Inference
        response = stub.GetInference(bentoml_service_pb2.Empty())
        print("Inference Data Head:")
        for row in response.data_head:
            print(row.row)
        print("Inference Predictions:", response.predictions)
        print("Inference RMSE:", response.rmse)


if __name__ == '__main__':
    run()
