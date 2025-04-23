from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
cdp = r"C:\Users\user\Desktop\chromedriver-win64\chromedriver.exe"  # Update this path
service = Service(cdp)

# Initialize the browser
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the page
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
driver.get(url)

# Wait for the close button to appear and click it
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "closeSpanId"))
    )
    close_button.click()
    print("Close button clicked.")
except Exception as e:
    print(f"An error occurred while clicking the close button: {e}")

# Wait for the page to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'clearfix.job-bx.wht-shd-bx'))  # Update with the correct class name
    )
    print("Job listings loaded.")
except Exception as e:
    print(f"An error occurred while waiting for job listings: {e}")
    driver.quit()
    exit()

# Open a file to save the job details
with open("job_listings.txt", "w") as file:
    # Find all job listings
    jobs = driver.find_elements(By.CLASS_NAME, 'clearfix.job-bx.wht-shd-bx')  # Update with the correct class name

    # Iterate over each job listing
    for job in jobs:
        try:
            # Extract the date
            date_element = job.find_element(By.CLASS_NAME, 'sim-posted')  # Update with the correct class name
            date = date_element.text.strip() if date_element else "N/A"

            # Extract the company name
            company_name_element = job.find_element(By.CLASS_NAME, 'joblist-comp-name')  # Update with the correct class name
            company_name = company_name_element.text.strip() if company_name_element else "N/A"

            # Extract the skills
            skills_element = job.find_element(By.CLASS_NAME, 'srp-skills')  # Update with the correct class name
            skills = skills_element.text.strip() if skills_element else "N/A"

            # Print job details to the terminal
            print(f"Company Name: {company_name}")
            print(f"Skills Required: {skills}")
            print(f"Posted: {date}")
            print('___' * 20)

            # Save job details to the file
            file.write(f"Company Name: {company_name}\n")
            file.write(f"Skills Required: {skills}\n")
            file.write(f"Posted: {date}\n")
            file.write('___' * 20 + '\n')
        except Exception as e:
            print(f"An error occurred while processing a job: {e}")

# Close the browser
driver.quit()
