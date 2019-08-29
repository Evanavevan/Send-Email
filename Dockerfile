FROM python:3.7.3-alpine3.9

RUN apk upgrade --update
RUN apk add bash

COPY ./requirements.txt /email-sender/requirements.txt

RUN pip3 install -r /email-sender/requirements.txt

COPY ./email_sender /email-sender/email_sender
COPY ./run.py /email-sender/run.py
EXPOSE 9995

ENTRYPOINT [ "python3", "/email-sender/run.py" ]
