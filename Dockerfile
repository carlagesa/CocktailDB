# pull official base image
FROM python:3.12-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
# Install build dependencies, install Python deps, then remove build deps
RUN apt-get update \
  && apt-get -y install --no-install-recommends gcc libpq-dev \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get purge -y --auto-remove gcc libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Create a user with UID 1000 and GID 1000
RUN groupadd -g 1000 appgroup && \
    useradd -r -u 1000 -g appgroup appuser

# Copy entrypoint script and make it executable
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Switch to this user
USER 1000:1000

# copy project
COPY . .

ENTRYPOINT ["entrypoint.sh"]
CMD ["gunicorn", "cocktaildb.wsgi:application", "--bind", "0.0.0.0:8000"]
