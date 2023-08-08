# Base Image
FROM python:3.8

# Work directory
WORKDIR /mlproject_telecom2

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy other project files

COPY . .

# Expose a port to Containers 
EXPOSE 8080

# Command to run on server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

