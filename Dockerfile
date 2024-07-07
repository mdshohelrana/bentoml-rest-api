FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV BENTOML_HOME=/bentoml
RUN bentoml build

CMD ["bentoml", "serve", "service.py:svc", "--production"]
