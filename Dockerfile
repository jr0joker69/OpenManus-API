FROM python:3.10-slim

# Set working directory (critical for imports)
WORKDIR /app

# Copy all project files into container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Start FastAPI using server.py (Render will inject PORT)
CMD ["python3", "server.py"]
