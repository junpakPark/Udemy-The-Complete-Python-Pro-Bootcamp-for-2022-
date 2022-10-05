import tkinter

FONT = ("Ariel", 24)

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=200)
window.config(padx=40, pady=20)

input = tkinter.Entry(width=20)
input.grid(row=0, column=1)

miles = tkinter.Label(text="Miles", font=FONT)
miles.grid(row=0, column=2)

is_equal_to = tkinter.Label(text="is_equal_to", font=FONT)
is_equal_to.grid(row=1, column=0)

km = tkinter.Label(text="km", font=FONT)
km.grid(row=1, column=2)

result = tkinter.Label(text="0", font=FONT)
result.grid(row=1, column=1)


def calculate():
    result.config(text=f"{round(float(input.get()) * 1.60934, 2)}")


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
