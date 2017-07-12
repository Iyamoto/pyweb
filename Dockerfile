FROM python:3.6.1-alpine

WORKDIR /usr/local/apps/pyweb

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt