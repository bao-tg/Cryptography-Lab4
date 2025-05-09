# Use official Python image
FROM python

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run init script and start Flask
CMD ["sh", "-c", "python init_db.py && python app.py"]
