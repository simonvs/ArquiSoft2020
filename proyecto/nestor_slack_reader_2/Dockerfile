FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1412446239478-1416130306645-WzhhKetklHBqyA25iaPLas4E"
ENV SLACK_SIGNING_SECRET="929e1515059e1a1a2f2162d4a059df78"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
