FROM python:3.6.1-alpine
MAINTAINER "iyamoto@gmail.com"
WORKDIR /code
ADD . /code
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python", "rnd.py"]