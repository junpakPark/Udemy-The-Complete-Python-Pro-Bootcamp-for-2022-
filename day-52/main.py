import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")

options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())


class InstaFollower:

    def __init__(self, service, options) -> None:
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        sleep(3)
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        sleep(1)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}"
        self.driver.get(url)
        followers_btn = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_T6"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()

        sleep(5)
        scrollbox = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbox)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(service, options)
bot.login()
bot.find_followers()
bot.follow()
