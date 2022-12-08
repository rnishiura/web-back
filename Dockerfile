# backend/web-back/Dockerfile
# set base image
FROM python:3.7

# set environment variables
ENV PYTHONDONTWRITEBYCCODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# copy project
COPY . ./

# exopse application port
EXPOSE 8000
