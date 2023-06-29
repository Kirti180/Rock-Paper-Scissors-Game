import random
import tkinter as tk
from tkinter import messagebox

options = ["rock", "paper", "scissor"]

def play_game():
    comCount = 0
    userCount = 0
    
    def get_user_choice(choice):
        nonlocal userCount, comCount
        userChoice = options[choice]
        comChoice = random.choice(options)
        lbl_user_choice.config(text="User Choice: " + userChoice)
        lbl_com_choice.config(text="Computer Choice: " + comChoice)
        
        if comChoice == userChoice:
            messagebox.showinfo("Result", "Game Draw")
            userCount += 1
            comCount += 1
        elif (userChoice == "rock" and comChoice == "scissor") or (userChoice == "paper" and comChoice == "rock") or (userChoice == "scissor" and comChoice == "paper"):
            messagebox.showinfo("Result", "You Win")
            userCount += 1
        else:
            messagebox.showinfo("Result", "Computer Wins")
            comCount += 1
        
        lbl_user_score.config(text="User Score: " + str(userCount))
        lbl_com_score.config(text="Computer Score: " + str(comCount))
        
        if userCount == 5 or comCount == 5:
            if userCount == comCount:
                result_message = "Game Draw"
            elif userCount > comCount:
                result_message = "You Win"
            else:
                result_message = "Computer Wins"
            
            final_message = f"Game Over\n\nFinal Score:\nUser: {userCount}\nComputer: {comCount}\n\n{result_message}"
            messagebox.showinfo("Game Over", final_message)
            window.quit()

    window = tk.Tk()
    window.title("Rock-Paper-Scissors Game")

    # Styling options
    window.configure(bg="#e3b009")
    window.geometry("400x300")
    window.resizable(False, False)
    title_font = ("Arial", 16, "bold")
    button_font = ("Arial", 12)
    label_font = ("Arial", 12)
    lbl_title = tk.Label(window, text="Rock-Paper-Scissors Game", font=title_font, bg="#13044f", fg="#ffffff")
    # lbl_title = tk.Label(window, text="Rock-Paper-Scissors Game", font=title_font, bg="#0a0a0a", color="#faf9f7")
    lbl_title.pack(pady=10)

    lbl_instructions = tk.Label(window, text="Select your choice:", font=label_font, bg="#F5F5F5")
    lbl_instructions.pack()

    btn_rock = tk.Button(window, text="Rock", command=lambda: get_user_choice(0), font=button_font, width=10, bg="#04d1b2")
    btn_rock.pack(pady=5)

    btn_paper = tk.Button(window, text="Paper", command=lambda: get_user_choice(1), font=button_font, width=10, bg="#04d1b2")
    btn_paper.pack(pady=5)

    btn_scissor = tk.Button(window, text="Scissor", command=lambda: get_user_choice(2), font=button_font, width=10, bg="#04d1b2")
    btn_scissor.pack(pady=5)

    lbl_user_choice = tk.Label(window, text="User Choice:", font=label_font, bg="#13044f", fg="#ffffff")
    lbl_user_choice.pack(pady=10)

    lbl_com_choice = tk.Label(window, text="Computer Choice:", font=label_font, bg="#13044f", fg="#ffffff")
    lbl_com_choice.pack(pady=10)

    lbl_user_score = tk.Label(window, text="User Score: 0", font=label_font, bg="#F5F5F5")
    lbl_user_score.pack(pady=10)

    lbl_com_score = tk.Label(window, text="Computer Score: 0", font=label_font, bg="#F5F5F5")
    lbl_com_score.pack(pady=10)

    window.mainloop()

play_game()
