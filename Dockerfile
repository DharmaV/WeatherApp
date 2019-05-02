# Using official python runtime base image
FROM python:3

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
COPY ./ /app


# Command to be run when launching the container
CMD ["python", "/app/Myfirst.py"]