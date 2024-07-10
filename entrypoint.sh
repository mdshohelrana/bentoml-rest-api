#!/bin/bash

# Start the gRPC server in the background
python grpc_server.py &
SERVER_PID=$!

# Wait for the gRPC server to start
echo "Waiting for gRPC server to start..."
sleep 10  # Adjust this time as necessary

# Run the gRPC client
python grpc_client.py

# Wait for the gRPC server process to finish
wait $SERVER_PID
