from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.python.org/"
driver.get(url)
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget p a")
# print(link.text)

# xpath = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
# print(xpath.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }

print(events)

# driver.quit()
