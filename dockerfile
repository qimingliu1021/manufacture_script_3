# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory to /app in the container
WORKDIR /app

# Install necessary tools and libraries
RUN apt-get update \
    && apt-get install -y wget gnupg2 software-properties-common unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update

# Install Google Chrome
RUN apt-get install -y google-chrome-stable

# Install Chromedriver
RUN CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f 3 | cut -d '.' -f 1) \
    && wget https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin/chromedriver \
    && chown root:root /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the CSV file into the container
COPY ./data/ /app/data/

# Make port 80 available to the world outside this container (optional)
EXPOSE 80

# Define environment variable (optional)
ENV NAME WebScraper

# Run script.py when the container launches
CMD ["python", "script.py"]
