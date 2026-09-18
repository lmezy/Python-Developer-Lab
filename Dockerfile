FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY app ./app
COPY scripts ./scripts
RUN pip install --no-cache-dir . && useradd --create-home --uid 10001 appuser && mkdir -p /app/data && chown -R appuser:appuser /app

USER appuser

VOLUME ["/app/data"]
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 CMD ["python", "-c", "import urllib.request; urllib.request.urlopen(\"http://127.0.0.1:8000/api/health\", timeout=3)"]

CMD ["sh", "-c", "python -m scripts.seed_content && exec uvicorn app.main:app --host 0.0.0.0 --port 8000"]
