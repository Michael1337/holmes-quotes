# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Run gunicorn to start the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
