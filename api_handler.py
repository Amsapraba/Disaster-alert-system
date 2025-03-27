import requests
import pandas as pd

# Fetch Earthquake data from USGS API
def get_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"
    response = requests.get(url)
    data = response.json()
    
    earthquakes = []
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        earthquakes.append({
            "magnitude": properties['mag'],
            "location": properties['place'],
            "time": pd.to_datetime(properties['time'], unit='ms'),
            "longitude": geometry['coordinates'][0],
            "latitude": geometry['coordinates'][1],
            "tsunami_alert": properties['tsunami']
        })
    return pd.DataFrame(earthquakes)

# Fetch Tsunami alerts from NOAA API
def get_tsunami_alerts():
    url = "https://api.weather.gov/alerts/active?event=tsunami"
    response = requests.get(url)
    data = response.json()
    
    alerts = []
    for alert in data['features']:
        properties = alert['properties']
        alerts.append({
            "title": properties['headline'],
            "description": properties['description'],
            "severity": properties['severity'],
            "area": properties['areaDesc'],
            "effective": properties['effective']
        })
    return pd.DataFrame(alerts)
