# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels -r requirements.txt

# Stage 2: Final Image
FROM python:3.12-slim

WORKDIR /usr/src/app

# Create a non-root user
RUN groupadd -g 1000 appgroup && \
    useradd -r -u 1000 -g appgroup appuser

# Copy installed packages from builder stage
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy entrypoint and project files
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
COPY . .

# Switch to non-root user
USER 1000:1000

ENTRYPOINT ["entrypoint.sh"]
CMD ["gunicorn", "cocktaildb.wsgi:application", "--bind", "0.0.0.0:8000"]
