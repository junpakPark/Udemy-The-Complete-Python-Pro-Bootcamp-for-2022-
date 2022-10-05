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
    save_text = f"{url} | {email} | {password}\n"

    if len(url) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Empty fields",
            message="PLZ.. Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=url,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?"
        )

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(save_text)
                web_input.delete(0, END)
                password_input.delete(0, END)


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
web_input = Entry(width=38)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()

name_input = Entry(width=38)
name_input.grid(row=2, column=1, columnspan=2)
name_input.insert(0, "email@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Button
generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
