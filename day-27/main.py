import tkinter

window = tkinter.Tk()
window.title("Hello")
window.minsize(width=500, height=300)
window.config(padx=20, pady=10)

# label
my_label = tkinter.Label(text="this is label", font=("Ariel", 24, "bold"))
# my_label.pack()
# my_label.pack(side="left")
my_label["text"] = "new text"
my_label.config(text="my text")
my_label.config(padx=50, pady=50)
my_label.grid(row=0, column=0)


# button
def button_clicked():
    print("I got clicked..")
    # my_label.config(text="Button Got Clicked...")
    my_label.config(text=f"{input.get()}")


button = tkinter.Button(text="click me..!", command=button_clicked)
button.config(padx=50, pady=50)
button.grid(row=1, column=1)
# button.pack()

new_button = tkinter.Button(text="new..!")
new_button.config(padx=50, pady=50)
new_button.grid(row=0, column=2)

# Entry
input = tkinter.Entry(width=20)
# input.pack()
input.grid(row=2, column=2)
# input.config(padx=50, pady=50)


window.mainloop()
