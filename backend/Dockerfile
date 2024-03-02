# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Start the application using Uvicorn with Dockerize to wait for the database
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
