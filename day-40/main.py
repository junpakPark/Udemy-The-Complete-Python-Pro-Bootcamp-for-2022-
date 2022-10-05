import os
import requests
from dotenv import load_dotenv

load_dotenv()


print("Welcome to Junpak's Flight Club.")
print("We find the best flight deals and email you.")


def sign_in():
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email\n")
    verify_email = input("Type your email again\n")
    if email == verify_email:
        url = os.environ["SHEETY_USER_API_URL"]
        body = {
            "user": {
                "First Name": first_name,
                "Last Name": last_name,
                "Email": verify_email,
            }
        }
        print(url)
        res = requests.post(url=url, json=body)
        res.raise_for_status()
        print("You're in the club")
    else:
        print("try again")
        sign_in()


sign_in()
