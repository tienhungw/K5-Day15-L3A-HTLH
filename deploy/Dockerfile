FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    WEB_HOST=0.0.0.0 \
    WEB_PORT=8085

COPY codebase/ ./codebase/
COPY data/lessons/ ./data/lessons/
COPY deploy/pages/ ./deploy/pages/

EXPOSE 8085

CMD ["python3", "codebase/web.py"]
