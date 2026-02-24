import tkinter as tk
from tkinter import messagebox

# Variables globales
current_player = "X"
board = [""] * 9

# Función cuando se hace clic en un botón
def button_click(index):
    global current_player
    
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        if check_winner():
            messagebox.showinfo("Game Over", f"Jugador {current_player} Ganador!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "¡Es un empate!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Función para verificar ganador
def check_winner():
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != "":
            return True
    return False

# Función para reiniciar
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x500")
root.configure(bg="#1e1e2f")

buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Helvetica", 24, "bold"),
        width=5,
        height=2,
        bg="#ffffff",
        fg="#1e1e2f",
        activebackground="#4CAF50",
        command=lambda i=i: button_click(i)
    )
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

title = tk.Label(root, text="TIC TAC TOE", 
                 font=("Helvetica", 18, "bold"), 
                 bg="#1e1e2f", 
                 fg="white")
title.grid(row=3, column=0, columnspan=3, pady=10)

reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Helvetica", 14, "bold"),
    bg="red",
    fg="white",
    command=reset_game
)
reset_button.grid(row=4, column=0, columnspan=3, pady=15)

root.mainloop()