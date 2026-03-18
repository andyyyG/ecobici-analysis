# Optimizing Bike Distribution in Mexico City: An Analysis of Ecobici Trip Data

## Overview

This project analyzes six months of historical trip data from ECOBICI — 
Mexico City's public bike-sharing system — to identify demand patterns 
across stations and time periods, with the goal of generating actionable 
insights for bike redistribution optimization.

**Key question:** How can ECOBICI optimize bicycle distribution across 
stations based on trip demand patterns?

📓 [View the full analysis on Kaggle]([https://www.kaggle.com/code/andyyyg/ecobici-data-analysis](https://www.kaggle.com/code/andyyyg/analysis-of-ecobici-trip-data))

---

## Dataset

- **Source:** [ECOBICI Open Data Portal](https://ecobici.cdmx.gob.mx/datos-abiertos/)
- **Period:** September 2025 – February 2026
- **Size:** ~9.4 million trips across 677 stations
- **Station metadata:** collected via the [GBFS API](https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json)

---

## Key Findings

1. **Demand follows a clear commuter pattern on weekdays** — with peaks at 8am 
and 6pm. Weekend demand is ~40% lower and follows a single midday peak, 
reflecting recreational rather than commuting use.

2. **The network is geographically polarized** — over 80% of activity is 
concentrated in Cuauhtémoc, which operates as the primary destination borough. 
Miguel Hidalgo (net flow: −125K) and Benito Juárez (−50K) function as origin 
boroughs, feeding bikes toward the city center each morning.

3. **Imbalance is widespread but asymmetric** — 369 out of 677 stations (55%) 
show a net bike deficit over the six-month period. Surpluses are highly 
concentrated in a few stations (CE-271-272 Jesús García: +42,816 net bikes), 
while deficits are distributed across many stations with moderate losses.

4. **Imbalances are time-specific and predictable** — the most severe 
network-wide deficit occurs at 7am on weekdays (net flow: −60K), immediately 
before the morning commute peak. Redistribution pressure is almost exclusively 
a weekday phenomenon.

5. **Route demand is highly dispersed** — with over 320,000 unique 
origin-destination pairs, the top 100 routes account for only 2.2% of all 
trips, confirming that redistribution must focus on station-level patterns 
rather than specific corridors.

---

## Recommendations

- **Prioritize pre-dawn restocking** of high-deficit stations in the 
Reforma/Polanco corridor before the 7–8am demand surge.
- **Use high-surplus stations as redistribution hubs** — particularly 
CE-271-272 and CE-266-267 Jesús García, which accumulate ~62,000 net 
bikes over six months.
- **Establish a Miguel Hidalgo → Cuauhtémoc redistribution corridor** 
to address the structural daily flow imbalance between boroughs.
- **Concentrate redistribution operations on weekdays** (Monday–Thursday) 
and shift to lighter maintenance schedules on weekends.

---

## Tools & Libraries

- Python 3.12
- pandas, numpy
- matplotlib, seaborn

---

## Author

**Andrea Gómez Franco** — [Kaggle](https://www.kaggle.com/andyyyg)
