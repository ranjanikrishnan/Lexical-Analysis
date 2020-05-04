FROM python:3.7
MAINTAINER Ranjani Krishnan "ranjanikrishnanr@gmail.com"
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt