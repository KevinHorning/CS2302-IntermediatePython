#9.23

from tkinter import Tk, Button, Label 
from tkinter.messagebox import showinfo
import random

boxPoint = 0
def newGame():
    #Come out roll
    total = random.randint(1, 6) + random.randint(1, 6)
    
    global boxPoint
    boxPoint = total
    displayLabel = Label(root, padx = 10, text = total)
    displayLabel.grid(row = 1, column = 0, columnspan = 2)

    if (total == 7 or total == 11):
        showinfo(message = "You win!")
    elif (total == 2 or total == 3 or total == 12):
        showinfo(message = "You rolled craps!")

        
def newRole():
    if (boxPoint == 0):
        showinfo(message = "Error: must make new game before rolling")
    else:    
        total = random.randint(1, 6) + random.randint(1, 6)
        displayLabel = Label(root, padx = 10, text = total)
        displayLabel.grid(row = 1, column = 0, columnspan = 2)
    
        if (total == boxPoint):
            showinfo(message = "You win!")
        elif (total == 7):
            showinfo(message = "You lose!")
        
root = Tk()

yourRollLabel = Label(root, padx = 10, text = "Your roll:")
displayLabel = Label(root, padx = 10, text = "")
newGameButton = Button(root, text = "New game", command = newGame)
rollButton = Button(root, text = "Roll for points", command = newRole)

yourRollLabel.grid(row = 0, column = 0, columnspan = 2)
displayLabel.grid(row = 1, column = 0, columnspan = 2)
newGameButton.grid(row = 2, column = 0)
rollButton.grid(row = 2, column = 1)

root.mainloop()    