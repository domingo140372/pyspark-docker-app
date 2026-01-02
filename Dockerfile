# Imagen base Python + Java (Java necesario para PySpark)
FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instalar Java y utilidades necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jre-headless build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements y código
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
RUN mkdir -p /data

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "app/main.py"]