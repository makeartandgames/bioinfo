# Start from the official Python 3.12 image
FROM python:3.12-slim

# Install gcc and other required build dependencies
RUN apt-get update && \
    apt-get install -y gcc build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
RUN pip install --no-cache-dir  setuptools
COPY . .
RUN python setup.py install
CMD ["sh"]
