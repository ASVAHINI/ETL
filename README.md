# Indiamart Data Collection and Analysis

## Project Overview

This project demonstrates how to collect product data from IndiaMART using a web scraper and perform basic data analysis using Python. The goal is to showcase the process of data extraction and analysis from an e-commerce platform.

---

## Step-by-Step Process

### 1. Data Collection Using a Web Scraper

To gather product information from IndiaMART, I utilized a web scraping tool. This scraper extracted details such as:

- Product names
- Company names
- Supplier locations

The collected data was saved into a CSV file named `Indiamart.csv`.

---

### 2. Data Analysis with Python

Using Python, I performed exploratory data analysis (EDA) on the collected dataset. The steps included:

- Loading the CSV file using `pandas`
- Removing duplicate entries
- Identifying the top 5 locations with the most suppliers
- Visualizing the supplier distribution using a bar chart with `matplotlib`

---

### 3. Insights from the Data

- The dataset contains 8 products from 7 different companies.
- Mumbai has the highest number of suppliers in this sample.
- The bar chart provides a clear visualization of supplier distribution across different locations.

- ### CHARTS
 ![output](https://github.com/user-attachments/assets/1678ee3c-3eb4-400c-b964-759950b6a429)
---

## Files Included

- `IndiaMart.csv`: The dataset containing the scraped product information.
- `pythonn.py`: The Python script used for data analysis.

---

## Tools Used

- Python 3
- pandas
- matplotlib
- Web scraping tool (chrome extension)
