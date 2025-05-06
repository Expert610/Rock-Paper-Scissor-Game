import tkinter as tk
import random

#Rock Paper Scissors Game
wins = 0
losses = 0
draw = 0
# Create GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="antique white")
win_label_var = tk.StringVar()
loss_label_var = tk.StringVar()
draw_label_var = tk.StringVar()

# Initial values
win_label_var.set(f"Wins: {wins}")
loss_label_var.set(f"Losses: {losses}")
draw_label_var.set(f"Draws: {draw}")
def update_labels():
    win_label_var.set(f"Wins: {wins}")
    loss_label_var.set(f"Losses: {losses}")
    draw_label_var.set(f"Draws: {draw}")
    
def play(user_choice):
    global wins, losses, draw
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Draw!"
        draw += 1
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "You Win!"
        wins += 1
    else:
        result = "You Lose!"
        losses += 1
        
    update_labels()
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
def reset_scores():
    global wins, losses, draw
    wins = 0
    losses = 0
    draw = 0
    update_labels()
    result_label.config(text="Scores reset!")
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
# Title label
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="antique white")
title.pack(pady=16)

# Result section
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="antique white")
user_label.pack()

computer_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="antique white")
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="antique white", fg="blue")
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="antique white")
button_frame.pack(pady=16)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Frame to hold all scores
result1 = tk.Frame(root, bg="antique white")
result1.pack(pady=10)


# Score title
tk.Label(result1, text="Your Score", font=("Arial", 14, "bold"), bg="antique white").pack(pady=(0, 10))

# Inner frame for score labels in a single row
score_row = tk.Frame(result1, bg="antique white")
score_row.pack()

# Three labels side by side
tk.Label(score_row, textvariable=win_label_var, font=("Arial", 12), fg="green", bg="antique white").pack(side="left", padx=15)
tk.Label(score_row, textvariable=loss_label_var, font=("Arial", 12), fg="red", bg="antique white").pack(side="left", padx=15)
tk.Label(score_row, textvariable=draw_label_var, font=("Arial", 12), fg="gray", bg="antique white").pack(side="left", padx=15)
button_row = tk.Frame(root, bg="antique white")
button_row.pack(pady=10)
reset_button = tk.Button(button_row, text="Reset Score", font=("Arial", 12), bg="lightgray", command=reset_scores)
reset_button.pack(side="left", padx=10)

quit_button = tk.Button(button_row, text="Quit Game", font=("Arial", 12), bg="lightgray", command=root.quit)
quit_button.pack(side="left", padx=10)



# Run the app
root.mainloop()
