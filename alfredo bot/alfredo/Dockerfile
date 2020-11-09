FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1412446239478-1416130306645-V90OkyJOjwoHrfkH1earcq3u"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /alfredo

COPY ./alfredobot.py /alfredobot.py
COPY ./alfredobot_app.py /alfredobot_app.py

CMD [ "python", "/alfredobot_app.py" ]
