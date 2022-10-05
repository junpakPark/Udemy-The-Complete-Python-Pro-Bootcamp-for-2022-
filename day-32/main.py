import smtplib
import datetime as dt
import random
import pandas


##################### Extra Hard Starting Project ######################
my_email = "test.junpak@gmail.com"
password = "punvhnamdosrfzun"

now = dt.datetime.now()
month = now.month
day = now.day

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")


for i in birthday_dict:
    if i["month"] == month and i["day"] == day:
        num = random.randint(1, 3)
        with open(f"letter_templates/letter_{num}.txt") as file:
            letter = file.read().replace("[NAME]", i["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{i['email']}",
                msg=f"Subject: HBD {i['name']}\n\n{letter}"
                )

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




