FROM python:3.7-alpine
MAINTAINER Erignoux Laurent <lerignoux@gmail.com>

RUN mkdir /app
ADD ./requirements.txt /app
RUN cd app && pip3 install -r requirements.txt
WORKDIR /app

ADD ./main.py /app

CMD python3 /app/main.py
