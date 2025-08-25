import streamlit as st
import sqlite3
import folium
from streamlit_folium import folium_static
import pandas as pd
import json

st.set_page_config(
    page_title="Kartoza DevOps App Argocd sync.",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling
st.markdown("""
<style>
.main {
    background-color: #F0F2F6;
}
h1 {
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# Connect to SQLite database
conn = sqlite3.connect('CT-TSMs.db')
query1 = """
SELECT PNT, geometry FROM town_survey_marks
"""
tsm_data = pd.read_sql(query1, conn)
query2 = """
SELECT OFC_SBRB_NAME, geometry FROM suburbs
"""
suburb_data = pd.read_sql(query2, conn)
conn.close()

# Parse the geometry data to extract coordinates
tsm_data['coordinates'] = tsm_data['geometry']
suburb_data['coordinates'] = suburb_data['geometry']

# Title of the dashboard
st.title('Kartoza Devops Testing App')
st.header('City of Kape Town TSM Browser Web App', divider="blue")
st.markdown("""
### Test Web App Overview
This TSM Browser Web App provides an interactive platform for users to explore Town Survey Marks (TSM) within the City of Cape Town.
Users can select a TSM from a dropdown menu or if they know the TSM ID, they can search for it, and the app will automatically zoom
in on the map to display the location.
""")


# Dropdown to select the location
suburb_option = st.sidebar.selectbox('Select a Suburb', suburb_data['OFC_SBRB_NAME'])
tsm_option = st.sidebar.selectbox('Select a Town Survey Mark', tsm_data['PNT'])

# Finding the coordinates
selected_mark = tsm_data[tsm_data['PNT'] == tsm_option]
selected_suburb = suburb_data[suburb_data['OFC_SBRB_NAME'] == suburb_option]
lat = json.loads(selected_mark["coordinates"].values[0])["coordinates"][1]
lon = json.loads(selected_mark["coordinates"].values[0])["coordinates"][0]
suburb_polygon_oiginal = json.loads(selected_suburb["coordinates"].values[0])["coordinates"][0][0]
suburb_polygon = []
for coord in suburb_polygon_oiginal:
    suburb_polygon.append(list(reversed(coord)))

# Create a map
m = folium.Map(location=suburb_polygon[0], zoom_start=13)

# Add marker
#folium.Marker([lat, lon], tooltip='Hi there I am a TSM', popup=tsm_option).add_to(m)
folium.Polygon(locations=suburb_polygon,tooltip='Hi there I am a suburb', popup=suburb_option, fill_color="blue", fill_opacity=0.3).add_to(m)

# Display the map
folium_static(m)
