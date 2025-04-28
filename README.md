# Grazioso Salvare – Rescue-Dog Dashboard  

**Author:** YOUR NAME      
**Course:** CS-340         
**Date:** MONTH DAY, YEAR  

---

## 1. Project Overview  

Grazioso Salvare trains dogs for specialized search-and-rescue work.  
This dashboard lets staff explore live shelter data stored in MongoDB and instantly filter for dogs that match the profile for:

| Rescue Type | Preferred Breeds | Sex | Age (weeks) |
|-------------|------------------|-----|-------------|
| Water Rescue | Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland | Intact Female | 26 – 156 |
| Mountain / Wilderness | German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, Rottweiler | Intact Male | 26 – 156 |
| Disaster / Individual Tracking | Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, Rottweiler | Intact Male | 20 – 300 |

Core widgets:

* **Interactive filters** (radio buttons)  
* **Dash DataTable** – sortable, paginated, searchable  
* **Pie chart** – distribution of breeds after filter  
* **Leaflet map** – pinpoints shelter location of selected dog  
* **Branding** – Grazioso Salvare logo → *www.snhu.edu* and author identifier  

Below are screenshots demonstrating the required functionality  
(*replace the placeholders with actual images or a screencast link*).

| Dashboard State | Screenshot |
|-----------------|------------|
| Start / Unfiltered | SCREENSHOT-START.PNG |
| Water Rescue | SCREENSHOT-WATER.PNG |
| Mountain / Wilderness | SCREENSHOT-MOUNTAIN.PNG |
| Disaster / Tracking | SCREENSHOT-DISASTER.PNG |
| Reset | SCREENSHOT-RESET.PNG |

> Or see the full flow in this screencast: **LINK-TO-VIDEO**

---

## 2. How to Run the Project  

1. **Clone / unzip** the project folder  
2. *(Optional but recommended)* Create and activate a virtual environment  
3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start MongoDB** (local or Atlas) and import the CSV if needed:

```bash
mongoimport --db aac --collection animals --type csv   --file aac_shelter_outcomes.csv --headerline
```

5. **Run the dashboard**

```bash
jupyter notebook ProjectTwoDashboard.ipynb
# or
jupyter lab ProjectTwoDashboard.ipynb
```

6. Execute the notebook → last cell launches the Dash server.  
   The dashboard opens automatically (default: `http://127.0.0.1:8050`).

> **Credentials** for the demo database  
> * Username: `aacuser`  
> * Password: `SNHU1234`

---

## 3. Technology Stack & Rationale  

| Layer | Tool | Why it was chosen |
|-------|------|------------------|
| **Model** | **MongoDB** | Flexible document model fits heterogenous shelter records; native geospatial indexes make map queries fast; PyMongo driver integrates easily with Python. |
| **Controller** | **Custom `crud.py` class** | Encapsulates Create/Read/Update/Delete operations; keeps database code separate from UI (MVC pattern). |
| **View / UI framework** | **Plotly Dash** | Pure-Python reactive web apps; integrates Plotly charts & Dash Leaflet, deploys in Jupyter or as standalone Flask server. |
| **Charts** | **Plotly Express** pie chart | Quick aggregation; auto-updates with callbacks. |
| **Map** | **Dash Leaflet** | Interactive OpenStreetMap tiles; supports marker pop-ups without external JS. |
| **DataTable** | **dash_table** | Built-in sorting, paging, CSV export; updates live from callbacks. |

---

## 4. Implementation Steps  

1. **Prototype** UI in Jupyter with static data  
2. **Build `AnimalShelter` CRUD class** (Project One)  
3. **Read & clean** Mongo data → Pandas DataFrame (drop `_id`)  
4. **Create filters** – radio items controlling three pre-written Mongo queries + reset  
5. **Link callbacks**  
   * Filter → update DataTable → update charts  
   * Row select → update Leaflet marker  
6. **Add branding** – logo (base64) + author tag  
7. **User-testing** – verified each filter returns expected dog count  
8. **Screenshots & README**  
9. **Packaged** project with `requirements.txt` for reproducibility  

---

## 5. Challenges & Solutions  

| Challenge | Resolution |
|-----------|------------|
| Dash Leaflet crashed when `_id` field present | Dropped `_id` column immediately after `pd.DataFrame.from_records()`. |
| Geolocation values sometimes missing | Added `.dropna(subset=['location_lat','location_long'])` before mapping to avoid null markers. |
| Table pagination reset after filter | Stored `page_current` & `page_size` in `State` and reset to first page on filter callback. |
| Credentials in notebook | Moved username/password to `crud.py`; notebook only passes them when instantiating the class. |

---

## 6. References / Resources  

* MongoDB documentation – https://docs.mongodb.com  
* Dash documentation – https://dash.plotly.com  
* Dash Leaflet – https://dash-leaflet.herokuapp.io  
* Austin Animal Center Outcomes dataset – https://data.austintexas.gov  
* SNHU CS-340 course materials  

---

## 7. License  

This project is released under the **MIT License** so that other non-profit rescue organizations can adapt the code for their own needs.

---
