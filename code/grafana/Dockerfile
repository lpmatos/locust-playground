FROM python:3.7.3-stretch

WORKDIR /app

# Copy source code to working directory
COPY . locustfile.py /app/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
    