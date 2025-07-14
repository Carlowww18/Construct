FROM python:3.13-slim

WORKDIR /area_admin

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean
    
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000