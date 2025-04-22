from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import logging

# Set up logging to a file
logging.basicConfig(filename="price_scraper.log", level=logging.INFO)

# Path to ChromeDriver
cdp = r"C:\Users\user\Desktop\chromedriver-win64\chromedriver.exe"
service = Service(cdp)

# Initialize the browser with options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.96 Safari/537.36")
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the page
url = 'https://www.amazon.com/AmazonBasics-Matte-Keyboard-QWERTY-Layout/dp/B07WJ5D3H4'
driver.get(url)

# Automatically handle CAPTCHA (if implemented in your earlier code)

def fetch_price():
    try:
        # Wait for the price element to be visible
        price_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "a-price-whole"))
        )
        price = price_element.text
        print(f"Price: {price}")
        logging.info(f"Price: {price}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

# Fetch the price every 30 seconds (to avoid overloading the website)
counter = 0
while counter < 10:  # Limit to 10 iterations for example
    fetch_price()
    counter += 1
    time.sleep(random.uniform(2, 5))  # Random delay between 2 and 5 seconds

driver.quit()
