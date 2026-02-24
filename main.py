import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x300")

label = tk.Label(root, text="Tic Tac Toe Game")
label.pack()

root.mainloop()

def check_winner(board):
    # TODO: Implement win logic
    pass