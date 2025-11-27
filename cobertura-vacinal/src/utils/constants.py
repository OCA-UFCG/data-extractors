import os

# The root of the data-extractors project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Path to the chromedriver executable for the cobertura-vacinal extractor.
CHROME_DRIVER_PATH = os.path.join(PROJECT_ROOT, "cobertura-vacinal", "chromedriver", "chromedriver")

# The directory where downloaded data from cobertura-vacinal is stored.
DOWNLOAD_PATH = os.path.join(PROJECT_ROOT, "cobertura-vacinal", "data")
print("path:", DOWNLOAD_PATH)
