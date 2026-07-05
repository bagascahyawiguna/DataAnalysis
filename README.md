# Bike Sharing Dashboard

Interactive data analysis dashboard exploring rental patterns from the [Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset), built as part of the "Belajar Analisis Data dengan Python" certification project from Dicoding Indonesia.

## Overview

This project analyzes 17,379 hourly and 731 daily bike-rental records (2011-2012) to uncover key rental drivers such as season, weather, time of day, and user type (casual vs registered). The analysis pipeline covers data wrangling, exploratory data analysis (EDA), and a manual user-segmentation study, all visualized through an interactive Streamlit dashboard.

## Key Insights

- Rentals peak in August, coinciding with the summer season
- Friday at 5 PM is the busiest hour of the week
- Clear weather and summer season show the highest rental volumes
- Registered users consistently rent more than casual users
- 2012 recorded higher overall rentals than 2011

## Tech Stack

- Python
- Pandas & NumPy (data wrangling)
- Matplotlib & Seaborn (visualization)
- Streamlit (interactive dashboard)

## Project Structure
DataAnalysis/
├── dashboard/
│   ├── dashboard.py       # Streamlit dashboard app
│   ├── day_cleaned.csv    # Cleaned daily rental data
│   └── hour_cleaned.csv   # Cleaned hourly rental data
├── data/
│   ├── day.csv             # Raw daily rental data
│   └── hour.csv             # Raw hourly rental data
├── notebook.ipynb          # Full data analysis notebook
├── requirements.txt
└── README.md

## Setup Environment

Clone this repository:
```bash
git clone https://github.com/bagascahyawiguna/DataAnalysis.git
cd DataAnalysis
```

Create and activate a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

## Run the Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

The dashboard will be available at `http://localhost:8501` in your browser.

## Author

Bagas Cahyawiguna
[LinkedIn](https://www.linkedin.com/in/bagas-cahyawiguna-539715285) · [GitHub](https://github.com/bagascahyawiguna)
