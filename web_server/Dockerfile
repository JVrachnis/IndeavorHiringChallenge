# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /web_code
COPY requirements.txt /web_code/
RUN pip install -r requirements.txt
COPY . /web_code/
