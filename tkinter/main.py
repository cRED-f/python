from tkinter import *

window = Tk()

window.title("my first GUI program")

window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# # label won't show up unless we use pack()
# my_label.pack(side="left")
# we can change label this two below ways
my_label["text"] = "New text"
my_label.config(text="New Text")
# my_label.place(x=100,y=50)
# grid and pack cant use same file
my_label.grid(column=1, row=0)


# when button got clicked text will be change
def button_clicked():
    new_label = input.get()
    my_label.config(text=new_label)


# button
button = Button(text="click me", command=button_clicked)
# button.pack()

# entry
input = Entry(width=10)
# input.pack()

window.mainloop()
