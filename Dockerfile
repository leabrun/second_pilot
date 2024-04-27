FROM python:3.9
WORKDIR /app

ENV token_tg=6958567737:AAHezDIF-Ow4DrRIxJ6JBErl-KvjtYzz7HU

RUN apt-get update && apt-get install

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .