# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY backend/ .

# Expose FastAPI default port
EXPOSE 8000

# Use a startup script that handles the PORT variable properly
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]