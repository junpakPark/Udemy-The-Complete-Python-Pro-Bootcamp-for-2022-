import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import pytz

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
stock_data = res1.json()

now = datetime.now(pytz.timezone("US/Eastern"))
weekday = now.weekday()

if weekday == 0:
    yesterday = (now - timedelta(3)).strftime("%Y-%m-%d")
    day_before_yesterday = (now - timedelta(4)).strftime("%Y-%m-%d")
elif weekday == 1:
    yesterday = (now - timedelta(1)).strftime("%Y-%m-%d")
    day_before_yesterday = (now - timedelta(4)).strftime("%Y-%m-%d")
elif weekday == 6:
    yesterday = (now - timedelta(2)).strftime("%Y-%m-%d")
    day_before_yesterday = (now - timedelta(3)).strftime("%Y-%m-%d")
else:
    yesterday = (now - timedelta(1)).strftime("%Y-%m-%d")
    day_before_yesterday = (now - timedelta(2)).strftime("%Y-%m-%d")


# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday_close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_close = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
stocks_return = round((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100, 2)


# # STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
url_news = "https://newsapi.org/v2/everything"
parameters_news = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

res2 = requests.get(url_news, parameters_news)
res2.raise_for_status()
news_data = res2.json()['articles'][:3]

if abs(stocks_return) > 5:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_=os.environ.get("TWILIO_VIRTUAL_NUMBER"),
            to=os.environ.get("TWILIO_VERIFIED_REAL_NUMBER")
            )
    print(message.status)


# # STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

