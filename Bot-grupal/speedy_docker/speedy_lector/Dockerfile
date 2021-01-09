FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN=""
ENV SLACK_SIGNING_SECRET=""

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /speedy_lector

COPY ./speedy_lector.py /speedy_lector.py

CMD [ "python", "/speedy_lector.py" ]
