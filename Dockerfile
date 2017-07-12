FROM python:3.6.1-alpine

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY rnd.py .

EXPOSE 8080
CMD ["python", "rnd.py"]