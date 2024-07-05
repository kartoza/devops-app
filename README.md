![Staging Tag](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/lgkgh/889dd6c34a68d9461b1fd8cdb56b8a21/raw/minisass_build-tag.json)
![Staging Status](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/lgkgh/889dd6c34a68d9461b1fd8cdb56b8a21/raw/minisass_build-status.json)

Kartoza DevOps Testing web-app
==========================

The Kartoza DevOps web-app is designed to serve as a simple testing web app for managing and evaluating changes within the Software Development Life Cycle (SDLC). Its primary purpose is to provide developers and DevOps teams with a simple, robust  scalable to deploy, test, and monitor web applications in a controlled setting.

## About the Web-App
The Web-App is a Streamlit Dashboard that is connected to an SQLite Database that holds a subset of the records of the Town Survey Marks situated in the Cape Town region. (The Data is courtsy of the [City of Cape Town's Open Data Portal](https://odp-cctegis.opendata.arcgis.com/datasets/4ee4fef293d74436afe31c2b979dfb30_14/about).) The web app makes it possible for user to select a TSM from a dropdown menu or if they know the TSM ID, they can search for it, and the app will automatically zoom 
in on the map to display it's location. 

## Usage
### 1. Clone the Repository:
```
git clone https://github.com/LokoMoloko98/Kartoza_Tech_Assessment.git
```

### 2. Navigate to the Project Directory:
```
cd /Kartoza_Tech_Assessment
```
### To be continued
...............

## Health Checks
- Dockerfile: A health check for the web-app container has been set up in in the Dockerfile to automatically check the health of the container. The health check makes a curl request internally so see if the Streamlit app is still accessible via ists local access url.
