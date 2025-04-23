----Amazon Price Tracker---

# Amazon Price Tracker

## Description:
This project is a Python-based script using Selenium to track the price of an Amazon product in real-time. It uses a headless Chrome browser to open the product page and scrape the price every 5 seconds, printing the current price to the terminal.

## Features:
- Tracks the price of a specified Amazon product
- Uses Selenium to automate the browser in headless mode (no UI)
- Prints the current price every 5 seconds

## Requirements:
- Python 3.x
- Selenium library
- Chrome WebDriver (for automating Chrome)
- Google Chrome browser

## How to Use:
1. Clone this repository or download the script.
2. Install the required Python libraries using pip:
    ```
    pip install selenium
    ```
3. Download the ChromeDriver that matches your version of Google Chrome from: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Replace the `cdp` variable in the script with the path to your downloaded `chromedriver.exe`.
5. Run the script by executing the following in your terminal:
    ```
    python Discount checker.py
    ```
6. The script will open the specified Amazon product page and track the price, printing the updated price to the terminal every 5 seconds.

---end---
# --- start ---
# README Section

"""
Python Job Scraper for TimesJobs
================================

This project is a Python-based web scraper designed to extract job listings from the TimesJobs website. 
Using Selenium, the scraper automates the process of navigating the website, closing popups, and extracting 
job details such as company name, required skills, and posting date. The extracted data is saved to a text 
file (`job_listings.txt`) for easy access and analysis.

Key Features:
-------------
1. Automates the process of navigating the TimesJobs website and closing popups.
2. Extracts job details such as:
   - Company Name
   - Required Skills
   - Posting Date
3. Saves the extracted data to a text file (`job_listings.txt`) for further use.
4. Handles dynamic web elements using Selenium's `WebDriverWait` and error handling.

How to Run:
-----------
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```bash
   pip install selenium
   Download the appropriate version of ChromeDriver for your Chrome browser version from: https://chromedriver.chromium.org/downloads
Update the cdp variable in the script with the path to your chromedriver.exe.
Run the script:
Check the job_listings.txt file for the extracted job details.
Example Output:
Company Name: ABC Technologies Skills Required: Python, Django, Flask Posted: Posted 3 days ago

Company Name: XYZ Solutions Skills Required: Python, Machine Learning Posted: Posted 2 days ago

Technologies Used:
Python
Selenium WebDriver
ChromeDriver
Purpose:
This project was created to automate the process of job searching and provide a structured way to analyze job listings. It can be extended to include additional features, such as filtering jobs based on specific criteria or integrating with other platforms.

"""

--- end ---

