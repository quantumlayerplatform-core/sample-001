# Use an official Python runtime as a parent image
FROM python:3.9-slim as builder

# Set the working directory in the builder stage
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --user -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Run tests
RUN python -m pytest

# Use a smaller base image for the runtime stage
FROM python:3.9-slim

# Set the working directory in the runtime stage
WORKDIR /usr/src/app

# Copy only the dependencies installation from the builder stage
COPY --from=builder /root/.local /root/.local

# Ensure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

# Copy the Flask application from the builder stage
COPY --from=builder /usr/src/app .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]