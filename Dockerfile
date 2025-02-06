FROM python:3.13-slim AS builder

RUN mkdir /app
WORKDIR /app
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
RUN pip install --upgrade pip  

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.13-slim

# Add a linus user and set the proper perms for the app
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

# Copy Python Deps from the build stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .
RUN python manage.py collectstatic --noinput

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Switch to non-root user
USER appuser

# Expose the Django port
EXPOSE 8000

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "hostelmeals.wsgi:application"]