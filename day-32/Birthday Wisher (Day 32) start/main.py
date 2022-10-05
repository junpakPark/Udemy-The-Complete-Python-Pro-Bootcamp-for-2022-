import smtplib
import datetime as dt
import random

my_email = "test.junpak@gmail.com"
password = "punvhnamdosrfzun"

now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with open("quotes.txt") as file:
        arr = file.readlines()

    msg = random.choice(arr)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test.junpak@yahoo.com",
            msg=f"Subject: monday quotes\n\n{msg}"
            )
