import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.87896193457031%2C%22east%22%3A-121.98769606542969%2C%22south%22%3A37.53582916124463%2C%22north%22%3A38.01398063431185%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
zillow_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

res = requests.get(zillow_url, headers=zillow_headers)
res.raise_for_status()
contents = res.text


soup = BeautifulSoup(contents, 'html.parser')

addresses = soup.select("ul li a address")
address_list = [address.getText() for address in addresses]

prices = soup.select(".kJFQQX span")
price_list = [price.getText().split('+')[0] for price in prices]

links = soup.select(".property-card-data a")
link_list = [f'https://www.zillow.com{link["href"]}' if "http" not in link["href"] else link["href"] for link in links]


options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


for i in range(len(address_list)):
    google_docs_url = "https://forms.gle/UzM7TpRJzCXPG3T99"

    driver.get(google_docs_url)
    sleep(2)

    q_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    
    sleep(2)
    q_address.send_keys(address_list[i])
    q_price.send_keys(price_list[i])
    q_link.send_keys(link_list[i])
    submit_btn.click()

driver.quit()
