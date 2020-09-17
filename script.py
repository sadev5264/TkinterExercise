from tkinter import *

window = Tk()


def convert_to_other_formats():
    weigh_in_kg = e1_kg.get()
    e1_grams.delete("1.0", END)
    e1_grams.insert(END, str(float(weigh_in_kg) * 1000) + " g")
    e2_pounds.delete("1.0", END)
    e2_pounds.insert(END, str(float(weigh_in_kg) * 2.20462) + " pounds")
    e3_ounces.delete("1.0", END)
    e3_ounces.insert(END, str(float(weigh_in_kg) * 35.274) + " ounces")


text = Label(window, height=1, width=50, text="Kg")
text.grid(row=0, column=0)

e1_kg = StringVar()

entry = Entry(window, textvariable=e1_kg)
entry.grid(row=0, column=1)

button = Button(window, text="Convert", command=convert_to_other_formats)
button.grid(row=0, column=2)

e1_grams = Text(window, height=1, width=50)
e1_grams.grid(row=1, column=0)
e2_pounds = Text(window, height=1, width=50)
e2_pounds.grid(row=1, column=1)
e3_ounces = Text(window, height=1, width=50)
e3_ounces.grid(row=1, column=2)

window.mainloop()
