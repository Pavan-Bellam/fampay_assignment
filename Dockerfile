FROM python:3.9-alpine3.16
LABEL maintainer = "pavan"

ENV pythonunbuffered 1

COPY ./requirements.txt /temp/requirements.txt
#COPY ./requirements.dev.txt /temp/requirements.dev.txt
COPY ./youtube_restapi /usr/src/app

WORKDIR /usr/src/app
EXPOSE 8000

ARG DEV="false"
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \ 
    /py/bin/pip install -r /temp/requirements.txt &&\
    rm -rf temp

ENV PATH="/py/bin:$PATH"
