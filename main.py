import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [""] * 9

def button_click(index):
    global current_player
    
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        if check_winner():
            messagebox.showinfo("Game Over", f"Jugador {current_player} gana!")
        elif "" not in board:
            messagebox.showinfo("Game Over", "Empate!")
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner():
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != "":
            return True
    return False

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    button = tk.Button(root, text="", width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()