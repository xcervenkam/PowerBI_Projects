# Online Retail Performance Dashboard

## Project Overview

This project analyzes transactional data from an online retail business in order to understand overall sales performance, customer behavior, and seasonal patterns.

The dashboard was built in Power BI and structured into three main analytical pages:

1. Executive Overview
2. Customer Segmentation & Behavior
3. Sales Seasonality & Weekend Patterns

The goal of the project was to create a business-focused interactive report that shows revenue trends, top-performing products and markets, customer concentration, order frequency behavior, and time-based sales patterns.

---

## Data Sources

### 1. Online Retail Transaction Data
Main dataset used for the project:

- `online_retail_II.xlsx`

The dataset contains transactional records such as:

- invoice number
- stock code
- product description
- quantity
- invoice date
- unit price
- customer ID
- country

### 2. Calendar / Holiday Data
A historical UK bank holidays file was explored during the project in order to test holiday-related analysis.

In practice, the final report focused primarily on:

- monthly seasonality
- weekday vs weekend patterns

This decision was made because weekend-related patterns were clearly present in the data, while direct holiday-day revenue patterns were not strong enough to be a central analytical story for the final dashboard.

---

## Tools Used

- Power BI
- Power Query
- DAX
- Excel / CSV-style transactional data
- Data modeling
- Customer-level summarization
- Interactive dashboard design

---

## Data Preparation

The retail transaction data was cleaned and transformed in Power Query.

Main preparation steps included:

- importing multiple yearly sheets from the Excel workbook
- appending them into one fact table
- renaming and standardizing columns
- converting data types
- creating `SalesAmount = Quantity * UnitPrice`
- creating `OrderDate`
- creating `OrderHour`
- identifying cancellations
- filtering invalid sales
- removing rows with missing customer IDs
- keeping only positive quantity and positive unit price transactions for the report version

A dedicated calendar table (`DimDate`) was created for time analysis.

A separate customer-level summary table (`CustomerSummary`) was created to support customer segmentation and order-frequency analysis.

---

## Data Model

The report is built around the following core tables:

### Fact Table
- `FactSales`

### Dimension Tables
- `DimDate`

### Helper / Summary Tables
- `CustomerSummary`
- `_Metrics`

### Key Model Logic
- `FactSales[OrderDate]` is related to `DimDate[Date]`
- `CustomerSummary` aggregates data to one row per customer
- `_Metrics` stores all main DAX measures

---

## Main DAX Measures

### Core Performance Metrics

```DAX
Revenue = SUM(FactSales[SalesAmount])
```

```DAX
Total Orders = DISTINCTCOUNT(FactSales[InvoiceNo])
```

```DAX
Total Customers = DISTINCTCOUNT(FactSales[CustomerID])
```

```DAX
Total Quantity = SUM(FactSales[Quantity])
```

```DAX
Average Order Value = DIVIDE([Revenue], [Total Orders], 0)
```

### Customer Metrics

```DAX
Revenue per Customer = DIVIDE([Revenue], [Total Customers], 0)
```

```DAX
Orders per Customer = DIVIDE([Total Orders], [Total Customers], 0)
```

```DAX
Quantity per Order = DIVIDE([Total Quantity], [Total Orders], 0)
```

```DAX
Top Customer Revenue Share % =
DIVIDE(
    MAXX(VALUES(FactSales[CustomerID]), [Revenue]),
    [Revenue],
    0
)
```

### Customer-Level Context Measures

```DAX
Customer Revenue = [Revenue]
```

```DAX
Customer Orders = [Total Orders]
```

### Weekend / Time Pattern Metrics

```DAX
Weekend Revenue =
CALCULATE(
    [Revenue],
    DimDate[IsWeekend] = 1
)
```

```DAX
Weekday Revenue =
CALCULATE(
    [Revenue],
    DimDate[IsWeekend] = 0
)
```

```DAX
Weekend Orders =
CALCULATE(
    [Total Orders],
    DimDate[IsWeekend] = 1
)
```

```DAX
Weekday Orders =
CALCULATE(
    [Total Orders],
    DimDate[IsWeekend] = 0
)
```

```DAX
Weekend Revenue Share % =
DIVIDE([Weekend Revenue], [Revenue], 0)
```

---

## Supporting Tables and Columns

### CustomerSummary table

A customer-level summary table was created to support segmentation and customer frequency analysis.

```DAX
CustomerSummary =
ADDCOLUMNS(
    SUMMARIZE(
        FactSales,
        FactSales[CustomerID]
    ),
    "Orders", CALCULATE(DISTINCTCOUNT(FactSales[InvoiceNo])),
    "Revenue", CALCULATE(SUM(FactSales[SalesAmount])),
    "Quantity", CALCULATE(SUM(FactSales[Quantity]))
)
```

### Order Frequency Buckets

```DAX
Order Frequency Bucket =
SWITCH(
    TRUE(),
    CustomerSummary[Orders] = 1, "1 order",
    CustomerSummary[Orders] <= 5, "2–5 orders",
    CustomerSummary[Orders] <= 10, "6–10 orders",
    CustomerSummary[Orders] <= 20, "11–20 orders",
    "21+ orders"
)
```

```DAX
Order Frequency Sort =
SWITCH(
    TRUE(),
    CustomerSummary[Orders] = 1, 1,
    CustomerSummary[Orders] <= 5, 2,
    CustomerSummary[Orders] <= 10, 3,
    CustomerSummary[Orders] <= 20, 4,
    5
)
```

### Date Table Columns

The `DimDate` table was extended with calendar attributes such as:

- Year
- Month
- MonthShort
- Quarter
- DayOfWeek
- DayOfWeekNumber
- IsWeekend
- DayType
- MonthYear
- MonthYearSort

This made it possible to build clean time-series and weekday/weekend analysis.

---

## Report Pages

### 1. Executive Overview

This page provides a high-level business summary of the retail dataset.

#### Main visuals
- Revenue
- Total Orders
- Total Customers
- Average Order Value
- Revenue Trend Over Time
- Top 10 Countries by Revenue
- Top 10 Products by Revenue
- Country slicer
- Month slicer

#### Analytical purpose
This page answers the most important summary questions:

- How much revenue was generated?
- How many orders and customers are represented?
- How does revenue evolve over time?
- Which countries generate the most revenue?
- Which products contribute the most to sales?

---

### 2. Customer Segmentation & Behavior

This page focuses on customer concentration and buying behavior.

#### Main visuals
- Revenue per Customer
- Orders per Customer
- Quantity per Order
- Top Customer Revenue Share %
- Top 10 Customers by Orders
- Top 10 Customers by Revenue
- Customer Value Distribution
- Customer Count by Order Frequency
- Country slicer
- Year slicer

#### Analytical purpose
This page helps identify:

- the most active customers
- the most valuable customers
- whether revenue is concentrated among a small group of customers
- how frequently customers place orders
- the structure of the customer base across low-frequency and repeat buyers

---

### 3. Sales Seasonality & Weekend Patterns

This page focuses on time-based sales behavior.

#### Main visuals
- Revenue
- Total Orders
- Weekend Revenue
- Weekend Revenue Share %
- Monthly Revenue Trend
- Monthly Order Trend
- Revenue by Day of Week
- Weekend vs Weekday Revenue
- Country slicer
- Year slicer

#### Analytical purpose
This page helps answer questions such as:

- How do revenue and orders evolve across months?
- Is there visible seasonality in the business?
- Which weekdays are strongest for revenue?
- How important are weekends compared with weekdays?
- Do time-based patterns remain consistent across years and countries?

---

## Key Insights the Dashboard Supports

The dashboard is designed to surface business insights such as:

- Revenue is concentrated in a relatively small group of customers.
- Customer frequency is uneven, with many lower-frequency buyers and a smaller repeat-customer base.
- Revenue and order counts follow visible seasonal patterns.
- Weekday and weekend performance differs meaningfully.
- A limited number of countries and products generate a large share of total sales.

---

## Folder Structure

```text
OnlineRetail_Project/
│
├── data_raw/
│   ├── online_retail_II.xlsx
│   └── bank-holidays / historical holiday files
│
├── pbix/
│   └── OnlineRetail_Report.pbix
│
├── screenshots/
│   └── dashboard screenshots
│
└── README.md
```

---

## Project Summary

This project turns raw online retail transactions into a structured Power BI dashboard focused on performance, customers, and seasonality.

The final dashboard provides a strong business-oriented view of:

- what drives revenue,
- who the most important customers are,
- how customer activity is distributed,
- and how sales behave over time.

It was built as a portfolio case study to demonstrate practical BI skills, DAX logic, customer analytics, and dashboard storytelling.
