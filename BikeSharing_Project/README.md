# Urban Bike Sharing Analytics Dashboard

## Project Overview

This project analyzes urban bike-sharing demand in New York City using Citi Bike trip data enriched with historical weather data.

The goal was to build an interactive Power BI dashboard exploring ride demand patterns, station performance, user behavior, and the impact of weather conditions on bike usage.

The final report consists of four analytical pages:

1. Executive Overview
2. Ride Behavior Over Time
3. Station & Geography Analysis
4. Weather Impact Analysis

---

## Data Sources

### Citi Bike Trip Data

Source: Citi Bike System Data  
Format: CSV files  
Period analyzed: January 2024 – March 2024

The dataset contains individual bike ride records, including:

- ride ID
- bike type
- start and end time
- start and end station
- station IDs
- latitude and longitude
- membership type

### Historical Weather Data

Source: Open-Meteo Historical Weather API  
Format: JSON

The JSON file was transformed in Power Query into an hourly weather table.

Weather variables used:

- temperature
- apparent temperature
- precipitation
- wind speed
- weather code

---

## Tools Used

- Power BI
- Power Query
- DAX
- CSV import
- JSON import
- Data modeling
- Geospatial visualizations

---

## Data Preparation

The Citi Bike CSV files were imported from a folder and combined into one fact table.

Main transformations included:

- combining monthly CSV files
- converting date and time columns
- calculating ride duration in minutes
- removing invalid or unrealistic rides
- creating date and hour columns
- creating a weather hour key

The weather JSON file was transformed from a nested structure into a structured hourly table.

---

## Data Model

Main tables used in the model:

### Fact Tables

- FactRides
- FactWeatherHourly

### Dimension Tables

- DimDate
- DimHour

### Measures Table

- _Metrics

Relationships were created between the fact tables and the date/hour dimensions.

---

## Key DAX Measures

### Ride Metrics

```DAX
Total Rides = COUNTROWS(FactRides)
```

```DAX
Average Ride Duration = AVERAGE(FactRides[DurationMinutes])
```
```DAX
Member Rides =
CALCULATE(
    [Total Rides],
    FactRides[member_casual] = "member"
)
```

```DAX
Casual Rides =
CALCULATE(
    [Total Rides],
    FactRides[member_casual] = "casual"
)
```

```DAX
Member Share % = DIVIDE([Member Rides], [Total Rides])
```

```DAX
Casual Share % = DIVIDE([Casual Rides], [Total Rides])
```

### Time Analysis Metrics


```DAX
Rides per Day =
AVERAGEX(
    VALUES(DimDate[Date]),
    [Total Rides]
)
```

```DAX
Max Daily Rides =
MAXX(
    VALUES(DimDate[Date]),
    [Total Rides]
)
```

```DAX
Min Daily Rides =
MINX(
    VALUES(DimDate[Date]),
    [Total Rides]
)
```

```DAX
Rolling 7D Avg =
AVERAGEX(
    DATESINPERIOD(
        DimDate[Date],
        MAX(DimDate[Date]),
        -7,
        DAY
    ),
    [Total Rides]
)
```
### Station Metrics

```DAX
Distinct Start Stations =
DISTINCTCOUNT(FactRides[start_station_id])
```


```DAX
Distinct End Stations =
DISTINCTCOUNT(FactRides[end_station_id])
```

### Weather Metrics

```DAX
Avg Temperature =
AVERAGE(FactWeatherHourly[temperature_2m])
```

```DAX
Avg Precipitation =
AVERAGE(FactWeatherHourly[precipitation])
```

```DAX
Avg Wind Speed =
AVERAGE(FactWeatherHourly[wind_speed_10m])
```

```DAX
Rides by Weather =
CALCULATE(
    [Total Rides],
    TREATAS(
        VALUES(FactWeatherHourly[WeatherHourKey]),
        FactRides[WeatherHourKey]
    )
)
```

A precipitation bucket column was created to analyze ride demand by precipitation intensity.

---

## Report Pages

### 1. Executive Overview

Main visuals:

- total rides
- average ride duration
- member share
- casual share
- daily ride trend
- hourly ride demand
- member vs casual rider comparison
- month and bike type slicers

### 2. Ride Behavior Over Time

Main visuals:

- rides per day
- maximum daily rides
- minimum daily rides
- 7-day rolling average
- ride demand by day of week
- ride intensity heatmap by weekday and hour

### 3. Station & Geography Analysis

Main visuals:

- ride origins map
- top 10 start stations
- top 10 destination stations
- distinct start stations
- distinct end stations
- date range slicer

### 4. Weather Impact Analysis

Main visuals:

- average temperature
- average precipitation
- average wind speed
- ride volume by precipitation bucket
- temperature vs ride volume over time
- wind speed vs ride volume over time
- date range slicer

---

## Folder Structure

```text
BikeSharing_Project/
│
├── data_raw/
│   ├── citibike/
│   └── weather/
│
├── pbix/
│   └── Power BI report file
│
└── screenshots/
    └── dashboard screenshots