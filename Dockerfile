
# Use a slim Python base image to reduce build size and avoid unauthorized pulls
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker layer caching. This way we only
# re-install dependencies when the requirements change.
COPY requirements.txt ./

# Install Python dependencies without caching to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port defined by Render (defaults to 8000) and run the FastAPI
# application using uvicorn. Render automatically sets the PORT environment
# variable; if not set, fall back to 8000.
ENV PORT=${PORT:-8000}
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
