# ---- GradeMind Dockerfile ----
# Uses Python 3.11 slim image for smaller size
# Installs dependencies and runs the Flask application

# Step 1: Use official Python 3.11 slim base image
FROM python:3.11-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files
COPY . .

# Step 6: Expose port 5000 (Flask default)
EXPOSE 5000

# Step 7: Set environment variables
ENV FLASK_SECRET_KEY=change-this-in-production
ENV PORT=5000

# Step 8: Run the Flask application
CMD ["python", "app.py"]
