FROM python:3.10-alpine3.16

COPY requirements.txt /src/requirements.txt
COPY . /src
WORKDIR /src
EXPOSE 8000
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /src/requirements.txt
RUN adduser --disabled-password admin
USER admin

