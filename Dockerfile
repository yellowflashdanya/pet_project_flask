# 1

FROM python:3.13-slim AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 2

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local

COPY /app .

CMD ["python", "app.py"]
