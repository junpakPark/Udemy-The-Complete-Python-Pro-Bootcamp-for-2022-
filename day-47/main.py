import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

load_dotenv()

url = "https://www.amazon.com/dp/B07HCLDN37?tag=camelproducts-20&linkCode=ogi&th=1&language=en_US"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}

res = requests.get(url=url, headers=headers)
res.raise_for_status()
contents = res.text

soup = BeautifulSoup(contents, "lxml")
# print(soup.prettify())
price_whole = soup.select_one("span.a-price-whole").getText()
price_fraction = soup.select_one("span.a-price-fraction").getText()
price_float = float(f"{price_whole}{price_fraction}")
print(price_float)

product_title = soup.select_one("span#productTitle").getText().split("|")[0].strip()
print(product_title)

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")


if price_float < 581:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: {product_title}: ${price_float} \n\n good good..."
            )
