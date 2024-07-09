import grpc
import logging
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)
        logging.info("Client is set up to communicate with the server at {}:{}".format(self.host, self.server_port))

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        logging.info(f'Sending message: {message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = UnaryClient()
    result = client.get_url(message="Hello Server, are you there?")
    logging.info(f'Received response: {result}')
