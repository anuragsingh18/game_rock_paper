import tkinter
import random
def rps(user):
    computer = random.randrange(1,4)
    if user == computer:
        var.set("It's a draw. \n No Points")  
    elif user == 1 and computer == 3:
        var.set("You chose Rock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
    elif user == 1 and computer == 2:
        var.set("You chose Rock, I chose Paper. \nYou lose")
        wins.set(wins.get() - 1)    
    elif user == 2 and computer == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
    elif user == 2 and computer == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        wins.set(wins.get() - 1)   
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        wins.set(wins.get() - 1)    
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
    else:
        var.set("Thanks for playing. \nYour Score is: " +str(wins.get()))


    
top = tkinter.Tk()
top.wm_title("RPS Python GUI")
top.minsize(width=350, height=150)
top.maxsize(width=350, height=250)
B1 = tkinter.Button(top, text ="Rock", command = lambda: rps(1))
B1.grid(row=0, column=1)
B2 = tkinter.Button(top, text ="Paper", command = lambda: rps(2))
B2.grid(row=0, column=2)
B3 = tkinter.Button(top, text ="Scissors", command = lambda: rps(3))
B3.grid(row=0, column=3)
B4 = tkinter.Button(top, text = "Resign", command = lambda: rps(4))
B4.grid(row=1)
# space = tkinter.Label(top, text="")
# space.grid(row=1)
var = tkinter.StringVar()
var.set('Welcome!')
l = tkinter.Label(top, textvariable = var)
l.grid(row=2, column=2)
wins = tkinter.IntVar()
wins.set(0)
w = tkinter.Label(top, textvariable = wins)
w.grid(row=4, column=2)
labeled = tkinter.Label(top, text = "Score:")
labeled.grid(row=3, column=2)
copy = tkinter.Label(top, text= "RPS GUI on Tkinter on Python")
copy.grid(row=5, column=2)
top.mainloop()