# Hong Kong Bus Routes

I wanted to get better at GeoGuessr specfically in HK but rural areas got too confusing.
Knowing the general location of bus routes across HK can help to narrow down where you are. :)

This code is based off the free data provided by data.gov.hk's bus routes

## Getting started
This project uses Python and the Folium module to create an HTML map.

1. Clone the Repository

```bash
git clone https://github.com/DTRW919/hkbusroutes.git
```

2. Install Folium with Pip

```bash
$ pip install Folium
```

3. Download and Insert the Dataset

You can find one [here](https://data.gov.hk/en-data/dataset/hk-td-tis_23-routes-fares-geojson).
Place it in `data/output.json`.

4. Run the create file

```bash
python createMap.py
```

Open the output map, which should be created in `output/map.html`.
