import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
PROMISED_DOWN = 500
PROMISED_up = 500


options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())

class InternetSpeedTwitterBot:

    def __init__(self, service, options) -> None:
        self.driver = webdriver.Chrome(service=service, options=options)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        self.driver.implicitly_wait(10)  # seconds
        start_btn = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a',
        )
        start_btn.click()
        sleep(45)  # seconds
        download_speed = self.driver.find_element(By.CSS_SELECTOR, '.result-data-value.download-speed').text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, '.result-data-value.upload-speed').text
        self.down = download_speed
        self.up = upload_speed

    def tweet_at_provider(self):
        url = "https://twitter.com/login"
        self.driver.get(url)
        sleep(1)  # seconds
        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys(ACCOUNT_EMAIL)
        username_input.send_keys(Keys.ENTER)
        sleep(3)  # seconds
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(ACCOUNT_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        sleep(2)  # seconds
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div')
        tweet_input.send_keys(f"{tweet}")


bot = InternetSpeedTwitterBot(service, options)
bot.get_internet_speed()
bot.tweet_at_provider()
