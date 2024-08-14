#USE python3.11
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run python script
CMD ["/bin/bash"]
#CMD ["python", "app.py"]