from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(url)

# xpath = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(xpath.text)

# korean = driver.find_element(By.LINK_TEXT, '한국어')
# korean.click()

# search = driver.find_element(By.NAME, 'search')
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

f_name = driver.find_element(By.NAME, 'fName')
f_name.send_keys("junpak")

l_name = driver.find_element(By.NAME, 'lName')
l_name.send_keys("park")

email = driver.find_element(By.NAME, 'email')
email.send_keys("test.junpak@gmail.com")

btn = driver.find_element(By.CSS_SELECTOR, 'button')
btn.click()
