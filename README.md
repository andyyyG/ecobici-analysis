# Optimizing Bike Distribution in Mexico City: An Analysis of Ecobici Trip Data

## Project Overview

This project analyzes 9.4 million ECOBICI trips in Mexico City to uncover demand patterns and optimize bike redistribution across the network.

The analysis identifies when and where bike shortages occur, why they happen, and how targeted operational strategies can significantly improve system efficiency.

**Key question:**  
How can ECOBICI optimize bicycle distribution across stations based on trip demand patterns?

View the full analysis on Kaggle:  
https://www.kaggle.com/code/andyyyg/analysis-of-ecobici-trip-data

---

## Business Problem

ECOBICI faces a common challenge in bike-sharing systems:

- Some stations run out of bikes (deficit)  
- Others become saturated (surplus)  

These imbalances reduce service reliability and require costly manual redistribution.

This project focuses on:
- Identifying imbalance patterns  
- Understanding their root causes  
- Proposing data-driven redistribution strategies  

---

## Dataset

- **Source:** [ECOBICI Open Data Portal](https://ecobici.cdmx.gob.mx/datos-abiertos/)
- **Period:** September 2025 – February 2026
- **Size:** ~9.4 million trips across 677 stations
- **Station metadata:** collected via the [GBFS API](https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json)

---

## Key Insights

- Demand is driven by commuting behavior  
  Clear peaks at 8AM and 6PM on weekdays, confirming that ECOBICI is primarily used for commuting rather than leisure.

- There is a strong directional flow in the network  
  Bikes consistently move from Miguel Hidalgo and Benito Juárez toward Cuauhtémoc, creating a structural imbalance.

- Bike shortages are widespread but predictable  
  55% of stations show deficits, but these follow consistent time-based patterns rather than random fluctuations.

- A small number of stations drive most of the imbalance  
  High-surplus stations accumulate bikes at a much higher rate than deficit stations lose them.

- Critical imbalance window occurs before peak demand  
  The system reaches its highest deficit at 7AM on weekdays, just before demand spikes.

---

## Recommendations

- Redistribute bikes before peak demand (5–6AM)  
  Prevent shortages during the most critical usage window.

- Use high-surplus stations as operational hubs  
  Reduce redistribution costs by centralizing bike collection points.

- Establish a structured redistribution flow  
  Move bikes from Cuauhtémoc back to Miguel Hidalgo and Benito Juárez overnight.

- Prioritize weekday operations  
  Focus resources where imbalance is most severe and predictable.

---

## Impact

This analysis shows that bike imbalances in ECOBICI are:

- Structural (driven by geography)  
- Predictable (driven by time)  
- Actionable (can be addressed with targeted interventions)  

By focusing on a small number of stations and critical time windows, ECOBICI can significantly improve bike availability without increasing operational complexity.

---

## Tools & Libraries

- Python 3.12
- pandas, numpy
- matplotlib, seaborn

---

## Author

**Andrea Gómez Franco** — [Kaggle](https://www.kaggle.com/andyyyg)
