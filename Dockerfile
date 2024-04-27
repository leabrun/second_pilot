FROM python:3.9
WORKDIR /app

ENV TG_TOKEN=6958567737:AAHezDIF-Ow4DrRIxJ6JBErl-KvjtYzz7HU

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .