import csv
import getpass
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Prompt for LinkedIn credentials
username = input("Enter your LinkedIn username: ")
password = getpass.getpass(prompt='Enter your LinkedIn password: ')

# Path to your ChromeDriver executable (same directory as the script)
script_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_path, 'chromedriver')

# Function to read company names from a file
def read_companies_from_file(file_path):
    with open(file_path, 'r') as file:
        companies = [line.strip() for line in file if line.strip()]
    return companies

# Function to generate LinkedIn URLs from company names
def generate_linkedin_urls(companies):
    base_url = 'https://www.linkedin.com/search/results/people/?company={}&network=%5B%22F%22%2C%22S%22%5D'
    return [(company, base_url.format(company.replace(' ', '%20'))) for company in companies]

def linkedin_login(driver):
    driver.get('https://www.linkedin.com/login')
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        ).send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'global-nav'))
        )
        print("Logged in successfully")
    except TimeoutException:
        print("Timeout while logging in")
        driver.quit()

def check_connections(driver, url):
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.entity-result__title-text'))
        )
        connections = driver.find_elements(By.CSS_SELECTOR, '.entity-result__title-text')
        first_connections = [conn for conn in connections if '1st' in conn.text]
        second_connections = [conn for conn in connections if '2nd' in conn.text]
        return len(first_connections), len(second_connections)
    except TimeoutException:
        print(f"Timeout while checking connections for URL: {url}")
        return 0, 0

def main():
    # Initialize the WebDriver
    options = webdriver.ChromeOptions()
    # Uncomment the following line to run in headless mode
    # options.add_argument('--headless')
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    linkedin_login(driver)

    # Read company names from file
    companies = read_companies_from_file('companies.txt')

    # Generate LinkedIn URLs
    urls = generate_linkedin_urls(companies)

    # Open CSV file for writing
    with open('linkedin_connections.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'LinkedIn URL', 'Number of 1st Connections', 'Number of 2nd Connections'])
        
        # Check each URL and write results to the CSV file
        for company, url in urls:
            first_connections, second_connections = check_connections(driver, url)
            writer.writerow([company, url, first_connections, second_connections])

    driver.quit()

if __name__ == "__main__":
    main()
