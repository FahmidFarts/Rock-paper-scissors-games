from tkinter import *
import random

def choice():
    user = entry.get().lower()
    computer = random.choice(options)
    if user == computer:
        result.config(text=f"Both chose {user}. It's a tie!")
    elif (user == "rock" and computer == "scissors"):
        result.config(text=f"Computer chose {computer}. You win!")
    elif (user == "paper" and computer == "rock"):
        result.config(text=f"Computer chose {computer}. You win!")
    elif (user == "scissors" and computer == "paper"):
        result.config(text=f"Computer chose {computer}. You win!")
    elif user == "nigger" or user == "nigga":
        result.config(text="You're the one who's black! Shut your fucking mouth bitch.")
    elif user == "":
        result.config(text="Please enter your choice!")
    elif user not in options:
        result.config(text="Invalid input! Please choose rock, paper, or scissors.")
    else:
        result.config(text=f"Computer chose {computer}. You lose!")



window = Tk()
window.geometry("620x300")
window.title("Rock Paper Scissors Game")
window.bind("<Return>", lambda event: choice())


options = ["rock","paper","scissors"]


lbl = Label(window,text="rock paper or scissors?: ",font=("add",20,"bold"))
lbl.pack()

entry = Entry(window,bd=5,font=("add",15))
entry.pack()

submit = Button(window,text="Submit",font=("add",15,"bold"),command=choice,bg="lightblue",fg="black",activebackground="lightblue",activeforeground="black")
submit.pack()

result = Label(window,font=("add",15,"bold"))
result.pack()

window.mainloop()