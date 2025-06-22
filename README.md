# Bitcoin Price Analysis Tool And Visualizer!!!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) 
![Pandas](https://img.shields.io/badge/Pandas-1.0+-brightgreen.svg) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)

A beginner-friendly Python application for fetching and analyzing Bitcoin price data from the last 7-14 days. Perfect for learning data visualization with Matplotlib and data manipulation with Pandas.

## Features
- Fetches Bitcoin price data for analysis
- Generates candlestick and line charts
- Stores raw and processed data for later use
- Simple command-line interface

## Getting Started
### Prerequisites
- Python 3.8+
- pip package manager

### Installation
1. Clone the repository: `git clone https://github.com/GSigioltzakis/bitcoin-price-analysis.git`
2. Navigate to project: `cd BITCOIN-VISUALIZER`
3. Install requirements: `pip install -r requirements.txt`

### Usage
Run the application with `python app.py`. This will fetch Bitcoin price data for the last 14 days, process it to create visualizations, and save both raw and processed data in the data directory.

## Scripts Overview
**fetch_price_data.py** retrieves Bitcoin price data and generates candlestick and line chart diagrams for the last 14 days, saving raw data to data/prices/last_7days_prices.csv.

**processes_data.py** processes the last 7 days of Bitcoin data, creates visualizations, and saves processed data to data/processed/candle_14days.csv and data/processed/chart_14days.csv.

## Learning Outcomes
This project helps beginners learn:
- Data visualization with Matplotlib
- Data manipulation with Pandas
- Python project organization
- File I/O operations with CSV
- Script modularization

## Requirements
Main dependencies: pandas and matplotlib (see requirements.txt for complete list)

## Contributing
Contributions are welcome! Great for Python beginners to start with open source.

## License
License George Sigioltzakhs 

Layout: 

project/
?
??? data/
    ??? prices/
        ??? last_7days_prices.csv
    ??? processed/
        ??? candle_14days.csv
        ??? chart_14days.csv
??? scripts/
?   ??? fetch_price_data.py
?   ??? processes_data.py
?
??? app.py
???README.md
???requirments.txt