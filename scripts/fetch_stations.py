"""
Fetches station information for ECOBICI (Mexico City's bike-sharing system)
from the GBFS API (General Bikeshare Feed Specification) and saves it as a CSV file.

The output includes station IDs, names, locations, and capacity,
which are used in subsequent preprocessing steps.
"""

import requests
import pandas as pd

url = "https://gbfs.mex.lyftbikes.com/gbfs/en/station_information.json"

data = requests.get(url).json()

stations = pd.DataFrame(data['data']['stations'])

stations.to_csv("ecobici_stations.csv", index=False)

print(f"Stations fetched: {len(stations):,}")
print(f"Saved to: ecobici_stations.csv")
