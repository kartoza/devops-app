import streamlit as st
import sqlite3
import folium
from streamlit_folium import folium_static
import pandas as pd
import json


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

suburb_option = st.sidebar.selectbox('Select a Suburb', suburb_data['OFC_SBRB_NAME'])
selected_suburb = suburb_data[suburb_data['OFC_SBRB_NAME'] == suburb_option]
suburb_polygon_oiginal = json.loads(selected_suburb["coordinates"].values[0])["coordinates"][0][0]
suburb_polygon = []
for coord in suburb_polygon_oiginal:
    suburb_polygon.append(list(reversed(coord)))

print(suburb_polygon)