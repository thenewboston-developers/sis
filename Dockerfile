# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Install the dependencies using Poetry
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . /app

# Expose any necessary ports
EXPOSE 80

# Run ia.py when the container launches
CMD ["poetry", "run", "python", "ia.py"]
