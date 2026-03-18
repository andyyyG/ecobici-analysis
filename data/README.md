# Data

The datasets used in this project are not stored in this repository due to file size.

## Trip data
- **Source:** [ECOBICI Open Data Portal](https://ecobici.cdmx.gob.mx/datos-abiertos/)
- **Period:** September 2025 – February 2026
- **Format:** 6 monthly CSV files
- **Also available on Kaggle:** [ecobici-trips-dataset-092025-to-022026](https://www.kaggle.com/datasets/andyyyg/ecobici-trips-dataset-092025-to-022026)

| Month | Direct download |
|-------|----------------|
| Sep 2025 | [2025-09.csv](https://ecobici.cdmx.gob.mx/wp-content/uploads/2025/10/2025-09.csv) |
| Oct 2025 | [2025-10.csv](https://ecobici.cdmx.gob.mx/wp-content/uploads/2025/11/2025-10-1.csv) |
| Nov 2025 | [2025-11.csv](https://ecobici.cdmx.gob.mx/wp-content/uploads/2025/12/2025-11.csv) |
| Dec 2025 | [2025-12.csv](https://ecobici.cdmx.gob.mx/wp-content/uploads/2026/01/2025-12.csv) |
| Jan 2026 | [2026-01.csv](https://ecobici.cdmx.gob.mx/wp-content/uploads/2026/02/2026-01.csv) |
| Feb 2026 | [2026-02.csv](https://ecobici.cdmx.gob.mx/wp-content/uploads/2026/03/2026-02.csv) |

## Station metadata
- **Source:** [GBFS API](https://gbfs.mex.lyftbikes.com/gbfs/en/station_information.json)
- **Format:** JSON via API, processed and saved as CSV
- **Also available on Kaggle:** [stations-metadata](https://www.kaggle.com/datasets/andyyyg/stations-metadata)

## Geographic boundaries (used in enrich_stations.py)

Two GeoJSON files from the Mexico City Open Data Portal were used to perform
spatial joins and assign municipality and neighborhood to each station:

| File | Description | Source |
|------|-------------|--------|
| `catlogo-de-colonias.json` | Neighborhood (colonia) boundaries | [datos.cdmx.gob.mx](https://datos.cdmx.gob.mx/dataset/02c6ce99-dbd8-47d8-aee1-ae885a12bb2f/resource/265d519b-8949-46c0-8caa-5eaca7e690ec/download/catlogo-de-colonias.json) |
| `limite-de-las-alcaldas.json` | Municipality (alcaldía) boundaries | [datos.cdmx.gob.mx](https://datos.cdmx.gob.mx/dataset/bae265a8-d1f6-4614-b399-4184bc93e027/resource/deb5c583-84e2-4e07-a706-1b3a0dbc99b0/download/limite-de-las-alcaldas.json) |
