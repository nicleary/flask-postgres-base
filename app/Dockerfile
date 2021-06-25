FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql libpq-dev python-dev uvicorn\
    && apt-get clean

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . ./