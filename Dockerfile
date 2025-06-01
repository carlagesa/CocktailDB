# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /cocktail-app

# Copy the requirements file into the container
COPY requirements.txt /cocktail-app/

# Install the dependencies from the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /cocktail-app/

# Expose the port the app will run on (e.g., 8000 for Django)
EXPOSE 8000

# Run the application (adjust to how you start your Django app)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#Adjusting for Production!
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cocktaildb.wsgi:application"] 

