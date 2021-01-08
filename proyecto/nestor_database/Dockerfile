FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_database

COPY ./nestor_database.py /nestor_database.py

CMD [ "python", "/nestor_database.py" ]