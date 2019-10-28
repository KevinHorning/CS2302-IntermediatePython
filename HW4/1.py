#HW Assignment 4
#2302 Python 2
#Professor Bowler
#3-26-19

#9.16

from tkinter import Tk, Button, Entry, Label, END 
from tkinter.messagebox import showinfo

def clicked():
    try:
        height = int(heightEntry.get())
        weight = int(weightEntry.get())
    except ValueError:
        showinfo(message = "Error, both height and weight need to be integers")
        heightEntry.delete(0, END)
        weightEntry.delete(0, END)
    else:
        showinfo(message = weight / (height * height))
        heightEntry.delete(0, END)
        weightEntry.delete(0, END)
        
root = Tk()

heightLabel = Label(root, padx = 10, text = "Enter your height(cm):")
weightLabel = Label(root, padx = 10, text = "Enter your weight(kg):")
heightEntry = Entry(root)
weightEntry = Entry(root)
button = Button(root, text = 'Compute BMI', command = clicked)

heightLabel.grid(row = 0, column = 0)
weightLabel.grid(row = 1, column = 0)
heightEntry.grid(row = 0, column = 1)
weightEntry.grid(row = 1, column = 1)
button.grid(row = 2, column = 0, columnspan = 2)

root.mainloop()
