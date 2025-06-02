FROM python:3.12.2 
ENV PYTHONBUFFERED=1
ENV PORT 8080
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run app with gunicorn command
CMD gunicorn cocktaildb.wsgi:application --bind 0.0.0.0:"${PORT}"

EXPOSE ${PORT}         