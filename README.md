# 📈 Financial Dashboard

Welcome to the **Financial Dashboard**, an interactive web application built with Streamlit that empowers users to visualize and analyze stock market data seamlessly.

##  Project Overview

This dashboard allows users to enter a stock ticker symbol (e.g., AAPL, MSFT, TSLA) and explore historical stock price data with customizable periods and intervals. Powered by Yahoo Finance and enhanced with Plotly visualizations, it provides clear insights through candlestick charts, moving averages, trading volume bars, and raw data tables.

## Key Features

- **Dynamic Stock Selection:** Enter any valid stock ticker symbol through an intuitive sidebar input.
- **Custom Time Frame:** Select data periods ranging from 1 month to 10 years.
- **Flexible Intervals:** Choose from daily, weekly, or monthly data aggregation.
- **Technical Indicators:** View 20-day and 50-day Simple Moving Averages (SMA) overlaid on candlestick charts.
- **Interactive Candlestick Chart:** Explore price action with rich, interactive Plotly visuals.
- **Volume Insight:** Track trading volume with an interactive bar chart.
- **Data Transparency:** Inspect the last 20 rows of raw stock data in a sortable, filterable table.
- **Data Export:** Download the displayed data as a CSV file for further analysis.

##  Technology Stack

- **Python** - Core programming language
- **Streamlit** - Web app framework for quick and beautiful UI
- **yfinance** - Fetches real-time and historical stock data
- **pandas** - Efficient data manipulation and analysis
- **plotly** - Advanced interactive charting library

##  How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Surabhi6300/Finacial_Dashboard.git
   cd Finacial_Dashboard
(Recommended) Create and activate a virtual environment:


```bash
python -m venv venv 
```
## Windows
```bash
.\venv\Scripts\activate
```
## macOS/Linux

source venv/bin/activate
Install dependencies:
Copy code
```bash
pip install -r requirements.txt
```
Launch the Streamlit application:
Copy code
```bash
streamlit run app.py
```
In the sidebar, enter your desired stock ticker and customize the period and interval to start visualizing!

 ## Project Structure
|-- app.py - Main application script containing Streamlit dashboard logic

|-- requirements.txt - Python dependencies

|-- .gitignore - Ignored files for Git

|-- .idea/ - IDE-specific files (PyCharm)

 ## Contribution
Contributions, suggestions, and improvements are most welcome! Feel free to fork the repository and open pull requests.

 Contact
Reach out to me on GitHub for any questions or feedback.

Unlock the power of financial insights with an easy-to-use dashboard—happy investing! 
