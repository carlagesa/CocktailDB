# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run gunicorn
# We'll use a placeholder for the Django project name for now
# Replace 'myproject' with the actual name of your Django project
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
