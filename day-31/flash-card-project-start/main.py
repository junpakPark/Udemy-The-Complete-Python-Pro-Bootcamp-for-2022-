from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data_dict = {}

# ---------------------------------------------------------------------------------------------------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict("records")
else:
    data_dict = data.to_dict("records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    french_word = random_word["French"]
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(card, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    English_word = random_word["English"]
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=English_word, fill="white")


def delete_word():
    data_dict.remove(random_word)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# # ---------------------------------------------------------------------------------------------------------------------#


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, flip_card)


# Photo Image
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)
right_btn = Button(image=right_img, highlightthickness=0, command=delete_word)
right_btn.grid(row=1, column=1)


next_card()


window.mainloop()
