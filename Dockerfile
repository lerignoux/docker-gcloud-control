FROM python:3.7-alpine
MAINTAINER Erignoux Laurent <lerignoux@gmail.com>

RUN mkdir /app
ADD ./requirements.txt /app
ADD ./main.py /app
RUN cd app && pip3 install -r requirements.txt
WORKDIR /app

RUN export GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

CMD python3 /app/main.py
