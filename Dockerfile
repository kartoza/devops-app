#Use an Ubuntu runtime as a parent image
FROM ubuntu:oracular

# Update packages 
RUN apt-get update

# Install Python3
RUN apt-get install python3 -y

# Install pip 

RUN apt-get install python3-pip -y

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python3 -m pip install -r requirements.txt --break-system-packages

# Convert the CT TSM geojson file into a table in an SQLite database file
RUN geojson-to-sqlite CT-TSMs.db town_survey_marks Town_Survey_Marks_1000.geojson 

RUN geojson-to-sqlite CT-TSMs.db town_survey_marks Official_Planning_Suburbs.geojson

# Make port 8501 available to the world outside this container
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run TSM_browser.py when the container launches
ENTRYPOINT ["streamlit", "run", "TSM_browser.py", "--server.port", "8501", "--server.address", "0.0.0.0", "--server.enableCORS", "false", "--server.enableWebsocketCompression=false"]