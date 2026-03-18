"""
Enriches ECOBICI station data with municipality (alcaldía) and neighborhood (colonia)
information using spatial joins with official Mexico City geographic boundaries.

Inputs:
    - ecobici_stations.csv: raw station data from the GBFS API
    - limite-de-las-alcaldas.json: municipality boundaries (GeoJSON)
    - catlogo-de-colonias.json: neighborhood boundaries (GeoJSON)

Output:
    - stations_info.csv: enriched station data with station_id, name,
      municipality, suburb, and capacity
"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

STATIONS_FILE  = 'ecobici_stations.csv'
ALCALDIAS_FILE = 'limite-de-las-alcaldas.json'
COLONIAS_FILE  = 'catlogo-de-colonias.json'

# Load stations
stations = pd.read_csv(STATIONS_FILE)
stations['geometry'] = stations.apply(
    lambda row: Point(row['lon'], row['lat']), axis=1
)
stations_gdf = gpd.GeoDataFrame(stations, geometry='geometry', crs="EPSG:4326")
print(f"Stations loaded: {len(stations_gdf):,}")

# Match municipalities via spatial join
alcaldias = gpd.read_file(ALCALDIAS_FILE).to_crs("EPSG:4326")

stations_alcaldias = gpd.sjoin(
    stations_gdf,
    alcaldias[['geometry', 'NOMGEO']],
    how='left',
    predicate='within'
)
stations_alcaldias = (stations_alcaldias
                      .drop(columns=['index_right'], errors='ignore')
                      .rename(columns={'NOMGEO': 'municipality'}))
stations_alcaldias['municipality'] = stations_alcaldias['municipality'].str.title()

# Match neighborhoods via spatial join
colonias = gpd.read_file(COLONIAS_FILE).to_crs("EPSG:4326")

stations_enriched = gpd.sjoin(
    stations_alcaldias,
    colonias[['geometry', 'colonia']],
    how='left',
    predicate='within'
)
stations_enriched = (stations_enriched
                     .drop(columns=['index_right'], errors='ignore')
                     .rename(columns={'colonia': 'suburb'}))
stations_enriched['suburb'] = stations_enriched['suburb'].str.title()

# Build final dataframe
final_df = stations_enriched[['station_id', 'name', 'municipality', 'suburb', 'capacity']]
final_df['municipality'] = final_df['municipality'].fillna('Unassigned')
final_df['suburb']       = final_df['suburb'].fillna('Unassigned')

print(f"\nFinal shape: {final_df.shape}")
print(f"Missing values:\n{final_df.isna().sum()}")

final_df.to_csv('stations_info.csv', index=False)
print(f"\nSaved to: stations_info.csv")
