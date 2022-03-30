from tkinter import *

root = Tk()
root.title("Protocap")

name = Label(root, text="Neeraj Kamboj")
name2 = Label(root, text="Mangala")

name.pack()
name2.pack()

in_box = Entry(root, bg="lightgreen")
in_box.pack()
in_box.insert(0, "Coordinates")


def greet():
    out = Label(root, text=f"You typed:, {in_box.get()}")
    out.pack()


in_button = Button(root, text="Enter coordinates", command=greet, padx=30, pady=10)
in_button.pack()

root.mainloop()
