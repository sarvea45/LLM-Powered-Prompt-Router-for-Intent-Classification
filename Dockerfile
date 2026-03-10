# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files (keeps it clean)
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure logs are printed immediately
ENV PYTHONUNBUFFERED 1

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your project files (app.py, classifier.py, prompts.json, etc.)
COPY . .

# Create the log file so Docker can write to it
RUN touch route_log.jsonl && chmod 666 route_log.jsonl

# The command to start your app
CMD ["python", "app.py"]