from tkinter import *

root = Tk()
root.title("Protocap")

name = Label(root, text="Neeraj Kamboj")

name.pack()

in_box = Entry(root, bg="lightgreen")
in_box.pack()


def greet():
    out = Label(root, text="You typed:" + in_box.get())
    out.pack()


in_button = Button(root, text="Enter coordinates", command=greet, padx=30, pady=10)
in_button.pack()

root.mainloop()
