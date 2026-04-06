FROM python:3.10-slim

WORKDIR /app

# Copy all project files into /app
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Start the FastAPI server using server.py
CMD ["python3", "server.py"]
