import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

url_stock = "https://www.alphavantage.co/query"
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}
res1 = requests.get(url_stock, parameters_stock)
res1.raise_for_status()
stock_data = res1.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yesterday_close = float(stock_list[0]["4. close"])
day_before_yesterday_close = float(stock_list[1]["4. close"])

stocks_return = round((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100, 2)
up_down = ""
if stocks_return > 0:
    up_down = "🔺"
elif stocks_return < 0:
    up_down = "🔻"
else:
    up_down = "_"


if abs(stocks_return) > 5:
    url_news = "https://newsapi.org/v2/everything"
    parameters_news = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    res2 = requests.get(url_news, parameters_news)
    res2.raise_for_status()
    news_top3_article = res2.json()['articles'][:3]

    msg_list = [f"{STOCK}: {up_down} {stocks_return}% Headline: {article['title']} \nBreif: {article['description']}" for article in news_top3_article]
    client = Client(account_sid, auth_token)
    for msg in msg_list:
        message = client.messages.create(
                body=msg,
                from_=os.environ.get("TWILIO_VIRTUAL_NUMBER"),
                to=os.environ.get("TWILIO_VERIFIED_REAL_NUMBER"),
                )
    print(message.status)
