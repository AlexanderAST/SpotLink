FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . . /app/

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]