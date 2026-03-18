"""
Merges monthly ECOBICI trip data with enriched station metadata.

For each monthly CSV file, departure and arrival station IDs are normalized
and matched against stations_info.csv to add station names, municipalities,
and neighborhoods to each trip record.

Input:
    - stations_info.csv: enriched station metadata
    - {YYYY-MM}.csv: raw monthly trip files from the ECOBICI open data portal

Output:
    - {YYYY-MM}_.csv: enriched monthly trip files ready for analysis
"""

import pandas as pd
import os

# Load station metadata
stations = pd.read_csv("stations_info.csv")
stations['station_id'] = stations['station_id'].astype(str).str.strip()

def normalize_id(value):
    """Normalize station IDs to a consistent integer string format."""
    if pd.isna(value):
        return None
    s = str(value).strip()
    if '-' in s:
        parts = [p.strip() for p in s.split('-')]
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return str(min(int(parts[0]), int(parts[1])))
    try:
        return str(int(s))
    except ValueError:
        return s

months = ["2025-09", "2025-10", "2025-11", "2025-12", "2026-01", "2026-02"]

for month in months:
    file = f"{month}.csv"
    if not os.path.exists(file):
        print(f"File not found: {file}")
        continue

    trips = pd.read_csv(file)

    # Normalize station IDs
    trips['id_departure'] = trips['Ciclo_Estacion_Retiro'].apply(normalize_id)
    trips['id_arrival']   = trips['Ciclo_EstacionArribo'].apply(normalize_id)

    # Merge departure station info
    trips = trips.merge(
        stations.rename(columns={
            'station_id' : 'id_departure',
            'name'       : 'departure_station_name',
            'municipality': 'departure_municipality',
            'suburb'     : 'departure_suburb'
        }),
        on='id_departure',
        how='left'
    )

    # Merge arrival station info
    trips = trips.merge(
        stations.rename(columns={
            'station_id' : 'id_arrival',
            'name'       : 'arrival_station_name',
            'municipality': 'arrival_municipality',
            'suburb'     : 'arrival_suburb'
        }),
        on='id_arrival',
        how='left'
    )

    trips = trips.drop(
        columns=['id_departure', 'id_arrival', 'capacity_x', 'capacity_y'],
        errors='ignore'
    )

    # Rename columns to English standard
    trips = trips.rename(columns={
        'Genero_Usuario'        : 'user_gender',
        'Edad_Usuario'          : 'user_age',
        'Bici'                  : 'bike_id',
        'Ciclo_Estacion_Retiro' : 'departure_station_id',
        'Fecha_Retiro'          : 'departure_date',
        'Hora_Retiro'           : 'departure_time',
        'Ciclo_EstacionArribo'  : 'arrival_station_id',
        'Fecha_Arribo'          : 'arrival_date',
        'Hora_Arribo'           : 'arrival_time',
    })

    output_file = f"{month}_.csv"
    trips.to_csv(output_file, index=False)
    print(f"Saved: {output_file}  ({len(trips):,} trips)")


