# Cobertura Vacinal - Data Extractor

This project contains a Python script to automatically extract vaccination coverage data from the Brazilian Ministry of Health's public information platform. It uses Selenium to navigate the web interface and download the data.

## How it Works

The script performs the following steps:

1.  Initializes a Chrome WebDriver using Selenium.
2.  Navigates to the official vaccination coverage page on the Ministry of Health's website.
3.  Selects the "Ocorrência" tab.
4.  Iterates through all available years and vaccines in the dropdown menus.
5.  For each year-vaccine combination, it clicks the "Exportar Dados" button to download the corresponding dataset.
6.  Saves the downloaded files to the `data/` directory.

## Prerequisites

Before running the script, ensure you have the following installed:

*   Python 3.x
*   The project dependencies listed in `requirements.txt`.
*   Google Chrome browser.
*   The appropriate version of ChromeDriver for your Chrome browser, located in the `chromedriver/` directory.

To install the Python dependencies, run:

```bash
pip install -r requirements.txt
```

## How to Run

To execute the data extraction script, navigate to the `src/` directory and run the `main.py` file:

```bash
cd src
python main.py
```

The script will open a new Chrome window and begin the automated extraction process. You can monitor the progress through the log messages printed in the console.

## Data Storage

All downloaded data files are stored in the `cobertura-vacinal/data/` directory. The script organizes the downloaded files by naming them according to the vaccine and year.
