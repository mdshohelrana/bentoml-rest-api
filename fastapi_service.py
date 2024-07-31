from fastapi import FastAPI, Depends
import bentoml

app = FastAPI()


@bentoml.service
@bentoml.mount_asgi_app(app, path="/v1")
class MyService:
    name = "MyService"

    @app.get('/hello')
    def hello(self):  # Inside service class, use `self` to access the service
        return f"Hello {self.name}"


@app.get("/hello1")
async def hello(service: MyService = Depends(bentoml.get_current_service)):
    # Outside service class, use `Depends` to get the service
    return f"Hello {service.name}"
