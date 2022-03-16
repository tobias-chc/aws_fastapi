FROM python:3.8-slim-buster

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

