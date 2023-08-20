import tkinter as tk
from tkinter import messagebox
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    return "Computer wins!"
def play_game(user_choice):
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    result = determine_winner(user_choice, computer_choice)
    message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\nResult: {result}"
    messagebox.showinfo("Game Result", message)
def on_rock_click():
    play_game("rock")
def on_paper_click():
    play_game("paper")
def on_scissors_click():
    play_game("scissors")
# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
# Create buttons
rock_button = tk.Button(root, text="Rock", command=on_rock_click)
paper_button = tk.Button(root, text="Paper", command=on_paper_click)
scissors_button = tk.Button(root, text="Scissors", command=on_scissors_click)
# Place buttons 
rock_button.pack(pady=50)
paper_button.pack(pady=50)
scissors_button.pack(pady=50)
# Start the GUI 
root.mainloop() 
play_again=input("paly again? (y/n): ")
if not play_again =="y":
    running=False
print("Thanks for playing")

