
# Quickstart

This quickstart demonstrates how to build a financial model service that provides stock price predictions and displays dataset information using BentoML. The service includes both REST API and gRPC endpoints.

## Prerequisites

Python 3.8+ and `pip` installed. See the [Python downloads page](https://www.python.org/downloads/) to learn more.

## Get started

Perform the following steps to run this project and deploy it to BentoCloud.

1. Install the required dependencies:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. Serve your model as an HTTP server. This starts a local server at [http://localhost:3000](http://localhost:3000/), making your model accessible as a web service.

   \`\`\`bash
   bentoml serve service.py:svc --reload
   \`\`\`

3. To serve the gRPC server, run the following command:

   \`\`\`bash
   python grpc/server.py
   \`\`\`

4. You can test the gRPC client by running:

   \`\`\`bash
   python grpc/client.py
   \`\`\`

5. Once your service is ready, you can deploy it to [BentoCloud](https://www.bentoml.com/cloud). Make sure you have [logged in to BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/how-tos/manage-access-token.html) and run the following command to deploy it.

   \`\`\`bash
   bentoml deploy .
   \`\`\`

   **Note**: Alternatively, you can manually build a Bento, [containerize it with Docker](https://docs.bentoml.com/en/latest/guides/containerization.html), and deploy it in any Docker-compatible environment.

## API Endpoints

### REST API

1. **Get Data Head**

   \`\`\`bash
   curl -X POST "http://127.0.0.1:3000/get_data_head"
   \`\`\`

2. **Get Prediction and MSE**

   \`\`\`bash
   curl -X POST "http://127.0.0.1:3000/predict" -H "Content-Type: application/json" -d '{}'
   \`\`\`

### gRPC API

1. **Get Data Head**

   Run the gRPC client:

   \`\`\`bash
   python grpc/client.py
   \`\`\`
