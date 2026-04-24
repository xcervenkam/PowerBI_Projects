# Premier League 2023/24 Player Analytics Dashboard

## Project Overview

This project analyzes player-level statistics from the 2023/24 Premier League season.

The goal was to create an interactive Power BI dashboard focused on player profiles, team composition, finishing performance, playmaking performance, and detailed player-level drill-through analysis.

The final report consists of three analytical pages:

1. Player Overview
2. Finishing & Playmaking Analysis
3. Detailed Player Analysis

The third page is designed as a detailed drill-through page that can be accessed from the second page.

---

## Data Source

### Premier League All Players Stats 23/24

Source: Kaggle  
Dataset: Premier League All Players Stats 23/24  
Format: CSV  
Files used:

- `data_raw/premier_league_23_24_raw.csv`
- `data_processed/premier_league_23_24_clean.csv`

The dataset contains player-level statistics for all footballers from the 2023/24 Premier League season.

---

## Project Structure

```text
PL_ Player_ Stats/
|- data_raw/
|  `- premier_league_23_24_raw.csv
|- data_processed/
|  `- premier_league_23_24_clean.csv
|- notebooks/
|  `- df_cleaning.ipynb
|- screenshots/
|  `- dashboard screenshots
|- Premier_League_Report.pbix
`- README.md
```

---

## Tools Used

- Python
- Pandas
- Jupyter Notebook
- Power BI
- Power Query
- DAX
- CSV data import
- Data cleaning
- Interactive dashboard design

---

## Data Preparation

The raw dataset was cleaned in a Jupyter Notebook using Python and Pandas.

Main cleaning steps included:

- loading the raw CSV file
- inspecting dataset shape and column names
- standardizing column names by converting them to lowercase and replacing spaces with underscores
- checking duplicates
- checking missing values
- cleaning the `nation` column
- cleaning the `pos` column
- validating numerical variables
- exporting the cleaned dataset as `data_processed/premier_league_23_24_clean.csv`

The final cleaned dataset contains:

- 580 rows
- 34 columns
- no missing values detected
- correctly assigned categorical and numerical data types

---

## Main Variables

The dataset contains player-level variables such as:

- `player` — player name
- `nation` — player nationality
- `pos` — player position
- `age` — player age
- `team` — Premier League club
- `mp` — matches played
- `starts` — number of starts
- `min` — minutes played
- `90s` — number of 90-minute equivalents played
- `gls` — goals scored
- `ast` — assists
- `g+a` — goals and assists combined
- `g-pk` — non-penalty goals
- `pk` — penalty goals
- `pkatt` — penalty attempts
- `crdy` — yellow cards
- `crdr` — red cards
- `xg` — expected goals
- `npxg` — non-penalty expected goals
- `xag` — expected assisted goals
- `npxg+xag` — non-penalty expected goals plus expected assisted goals
- `prgc` — progressive carries
- `prgp` — progressive passes
- `prgr` — progressive runs
- `xg+xag` — expected goals plus expected assisted goals

---

## Data Validation

During the cleaning process, the numerical variables were checked for consistency.

Key validation findings:

- the dataset contains 580 players
- the maximum number of matches played is 38, which matches a full Premier League season
- the maximum number of minutes played is 3,420, which corresponds to 38 full 90-minute matches
- the maximum number of goals is 27, which is realistic for the 2023/24 season
- the player age range is from 15 to 38
- some per-90 metrics contain high values for low-minute players, which is expected and should be handled through report filters when needed

---

## Power BI Data Model

The Power BI report is based mainly on the cleaned table:

- `premier_league_23_24_clean`

A separate measures table was used for DAX measures.

The dashboard uses slicers and drill-through navigation to allow interactive player, team, and position-level analysis.

---

## Key DAX Measures

### Goals Over xG

```DAX
Goals Over xG =
SUM(premier_league_23_24_clean[gls])
    - SUM(premier_league_23_24_clean[xg])
```

This measure compares actual goals scored against expected goals.

Positive values indicate finishing overperformance, while negative values indicate underperformance relative to xG.

---

### Assists Over xAG

```DAX
Assists Over xAG =
SUM(premier_league_23_24_clean[ast])
    - SUM(premier_league_23_24_clean[xag])
```

This measure compares actual assists against expected assisted goals.

Positive values indicate playmaking overperformance, while negative values indicate underperformance relative to xAG.

---

### Goals + Assists per 90

```DAX
G + A per 90 =
DIVIDE(
    SUM(premier_league_23_24_clean[gls])
        + SUM(premier_league_23_24_clean[ast]),
    SUM(premier_league_23_24_clean[90s]),
    0
)
```

This measure calculates attacking output per 90 minutes.

It allows comparison between players with different playing time.

---

## Report Pages

## 1. Player Overview

The first report page provides a general overview of Premier League players in the 2023/24 season.

### Main visuals

- average player age
- total number of players
- mean age by position
- player country map
- player table
- position slicer
- team slicer

### Purpose

This page gives a quick overview of the dataset and allows filtering players by position and team.

It helps answer questions such as:

- How many players are included in the dataset?
- What is the average age of Premier League players?
- Which positions have older or younger players on average?
- Which countries are represented in the league?
- Which players belong to each team and position?

---

## 2. Finishing & Playmaking Analysis

The second report page focuses on attacking performance, especially finishing and chance creation.

### Main visuals

- Goals vs xG scatter plot
- Top finishing overperformers
- Assists vs xAG scatter plot
- Playmaking efficiency chart
- team slicer

### Purpose

This page analyzes how players performed compared to expected metrics.

It helps identify:

- players who scored more goals than expected
- players who underperformed their xG
- players who created more assists than expected
- players with strong playmaking efficiency
- team-level attacking profiles

The page also acts as the main analytical page from which users can click through to the detailed player analysis page.

---

## 3. Detailed Player Analysis

The third report page provides detailed drill-through analysis for a selected player.

It can be accessed from the Finishing & Playmaking Analysis page.

### Main visuals

- selected player name
- Goals vs xG gauge
- Assists vs xAG gauge
- matches played
- minutes played
- goals
- xG
- assists
- team
- country
- age
- position

### Purpose

This page provides a player-specific analytical profile.

It helps answer questions such as:

- How many minutes did the selected player play?
- How many goals and assists did the player record?
- Did the player outperform or underperform expected goals?
- Did the player outperform or underperform expected assists?
- What is the player's team, nationality, age, and position?

---

## Project Summary

This Power BI project analyzes 580 Premier League players from the 2023/24 season.

The report combines general player overview analysis with deeper attacking performance analysis based on goals, assists, xG, and xAG.

The dashboard allows users to explore player profiles, compare actual and expected attacking performance, identify overperformers and underperformers, and drill through to detailed individual player analysis.

This project was created as a Power BI portfolio case study to demonstrate practical skills in data cleaning, DAX, dashboard design, and sports analytics.
