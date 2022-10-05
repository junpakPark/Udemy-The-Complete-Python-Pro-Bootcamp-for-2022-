import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    url = web_input.get()
    email = name_input.get()
    password = password_input.get()
    new_data = {
        url: {
            "email": email,
            "password": password
        }
    }

    if len(url) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty fields",
            message="PLZ.. Don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # redaing old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # saving updated data
                json.dump(data, file, indent=4)

        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------- Find password ----------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as file:
            # redaing old data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning("Error", "There is no data file in directory")
    
    else:
        url = web_input.get()
        if url in data:
            messagebox.showinfo(
                url,
                f"Email: {data[url]['email']} \n Password: {data[url]['password']}"
                )
        else:
            messagebox.showwarning("Error", f"No details for {url} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Label
web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

name_label = Label(text="Email/Username: ")
name_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entry
web_input = Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()

name_input = Entry(width=38)
name_input.grid(row=2, column=1, columnspan=2)
name_input.insert(0, "email@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Button
generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(row=3, column=2)

search_btn = Button(text="Search", width=13, command=find_password)
search_btn.grid(row=1, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
