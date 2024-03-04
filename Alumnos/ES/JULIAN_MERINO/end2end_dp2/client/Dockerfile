FROM python:3.8.16-slim

WORKDIR /app

COPY /client/main.py main.py
COPY /client/data data
COPY /client/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "-u", "main.py" ]