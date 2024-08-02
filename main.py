from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up Chrome options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

companies = ['Google', 'Microsoft', 'Amazon']  # Example companies

job_listings = []

for company in companies:
    driver.get('https://www.linkedin.com/jobs')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.jobs-search-box__text-input')))

    search_box = driver.find_element(By.CSS_SELECTOR, 'input.jobs-search-box__text-input')
    search_box.send_keys(company)
    search_box.submit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.jobs-search__results-list li')))

    job_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.jobs-search__results-list li')

    for job in job_elements[:10]:  # Limiting to first 10 jobs
        try:
            title = job.find_element(By.CSS_SELECTOR, 'span.screen-reader-text').text
            location = job.find_element(By.CSS_SELECTOR, 'span.job-search-card__location').text
            job_listings.append({
                'company': company,
                'title': title,
                'location': location
            })
        except Exception as e:
            print(f"Error scraping job data: {e}")

driver.quit()

# Convert to DataFrame
df_jobs = pd.DataFrame(job_listings)
df_jobs.to_csv('job_listings.csv', index=False)
df_jobs.to_json('job_listings.json', orient='records')
