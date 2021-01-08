FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1412446239478-1416130306645-WzhhKetklHBqyA25iaPLas4E"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /speedy_escritor

COPY ./speedy_escritor.py /speedy_escritor.py

CMD [ "python", "/speedy_escritor.py" ]
