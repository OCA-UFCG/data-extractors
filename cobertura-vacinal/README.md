# Cobertura Vacinal - Data Extractor

**Data Source:** [Infoms Saude - Gov.br](https://infoms.saude.gov.br/extensions/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_RESIDENCIA/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_RESIDENCIA.html) 

This project contains a Python script to automatically extract vaccination coverage data from the [Brazilian Ministry of Health's public information platform](https://infoms.saude.gov.br/extensions/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_RESIDENCIA/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_RESIDENCIA.html). It uses Selenium to navigate the web interface and download the data.

## How it Works

The script performs the following steps:

1.  Initializes a Chrome WebDriver using Selenium.
2.  Navigates to the official vaccination coverage page on the Ministry of Health's website.
3.  Selects the "Dados" tab.
4.  Iterates through all available years and vaccines in the dropdown menus.
5.  For each year-vaccine combination, it clicks the "Exportar Dados" button to download the corresponding dataset.
6.  Saves the downloaded files to the `data/` directory.

## How to Run

You can run the data extraction script in two ways: using Docker (recommended) or running it manually.

### With Docker (Recommended)

#### Prerequisites

Before running the script, ensure you have the following installed:
* [Docker](https://docs.docker.com/engine/install/)
* [Docker compose](https://docs.docker.com/compose/install/)

#### Running

This is the easiest and recommended way to run the script, as it automatically sets up the entire environment for you.

1.  Ensure you have Docker and Docker Compose installed.
2.  From the `cobertura-vacinal` directory, run the following command:

    ```bash
    docker-compose up
    ```

This will build the necessary Docker images and start the data extraction process. You can monitor the progress through the log messages printed in the console.

### Manually

#### Prerequisites

Before running the script, ensure you have the following installed:

*   Python 3.x
*   The project dependencies listed in `requirements.txt`.
*   Google Chrome browser and the appropriate version of ChromeDriver (for manual execution).
*   Docker and Docker Compose (for containerized execution).

#### Running

If you prefer to run the script without Docker, you can follow these steps:

1.  Install the Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have Google Chrome and the correct version of [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) for your browser in the `chromedriver/` directory. (The script is configured to look for it there).

3.  To execute the data extraction script, navigate to the `cobertura-vacinal/` directory and run the `main.py` file:

    ```bash
    python main.py
    ```

The script will open a new Chrome window and begin the automated extraction process.

## Data Storage

All downloaded data files are stored in the `cobertura-vacinal/data/` directory. The script organizes the downloaded files by naming them according to the vaccine and year.

## Logging

The script logs its progress and any errors to both the console and a log file.
All log files are stored in the `cobertura-vacinal/logs/` directory, with the main log file named `cobertura-vacinal.txt`.
The console output is color-coded for better readability, while the log file contains detailed, timestamped messages that can be used for debugging and tracking the script's execution over time.

