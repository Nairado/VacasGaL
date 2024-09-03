FROM python:3.12.5-slim

ARG BCK_WORKDIR
ARG BCK_PORT

WORKDIR ${BCK_WORKDIR}

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${BCK_PORT}