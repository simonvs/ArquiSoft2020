FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1412446239478-1416130306645-WzhhKetklHBqyA25iaPLas4E"
ENV SLACK_SIGNING_SECRET="b823f65b21f7ee34b5680a1e36d8f239"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /speedy_lector

COPY ./speedy_lector.py /speedy_lector.py

CMD [ "python", "/speedy_lector.py" ]
