# Use slim Python base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install git (needed if you have any git dependencies)
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python code
COPY uploader/ uploader/

# Use ENTRYPOINT so that args passed to `docker run` go to your script
ENTRYPOINT ["python", "uploader/s3_uploader.py"]

