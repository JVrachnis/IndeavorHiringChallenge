# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /api_code
COPY requirements.txt /api_code/
RUN pip install -r requirements.txt
COPY . /api_code/
