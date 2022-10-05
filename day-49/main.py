import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")

options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3254974208&f_AL=true&geoId=105149562&keywords=Java%20Software%20Engineer&location=대한민국&refresh=true"
driver.get(url)

sign_in = driver.find_element(By.LINK_TEXT, '로그인')
sign_in.click()

driver.implicitly_wait(10)  # seconds

email_input = driver.find_element(By.NAME, "session_key")
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.NAME, "session_password")
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)


# companies = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
# for company in companies:
#     try:
#         driver.implicitly_wait(10)  # seconds
#         company.click()
#         driver.implicitly_wait(10)  # seconds
#         save_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
#         save_btn.click()

#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    #Try to locate the apply button, if can't locate then skip the job.
    try:
        # apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        # apply_button.click()
        # time.sleep(5)
        save_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
        save_btn.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
