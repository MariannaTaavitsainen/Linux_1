# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]
