import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class TicTacToeGUI:
    def __init__(self, master, size=3, mode='P', name='main player', second='second player'):
        self.master = master
        self.computer_name = "Computer"
        self.name = name
        self.second = second
        self.mode = mode
        self.master.title("TicTacToe")
        self.board_size = size
        self.current_player = "X"
        self.players = {"X": name, "O": self.computer_name} if mode == 'C' else {"X": name, "O": second}
        self.wins_losses = {"X": 0, "O": 0}
        self.board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.create_board()
        self.start_time = 0
        self.first_move = True

    def create_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self.master, text="", font=("Times New Roman", 20), width=4, height=1,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def handle_click(self, row, col):
        if self.board[row][col] == " ":
            self.make_move(row, col)

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        if self.first_move:
            self.start_time = time.time()
            self.first_move = False
        if self.check_win(self.current_player):
            end_time = time.time()
            elapsed_time = round(end_time - self.start_time, 2)
            winner = self.players[self.current_player]
            self.wins_losses[self.current_player] += 1
            messagebox.showinfo("Winner", f"{winner} wins in {elapsed_time} seconds!")
            self.record_high_score(self.current_player)
            self.reset_board()
        elif self.is_board_full():
            messagebox.showinfo("Draw", "It's a draw!")
            self.reset_board()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.mode == 'C' and self.current_player == 'O':
                self.computer_move_rand()

    def computer_move_rand(self):
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def check_win(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(self.board_size):
            if all(self.board[row][col] == player for row in range(self.board_size)):
                return True
        if all(self.board[i][i] == player for i in range(self.board_size)) or \
           all(self.board[i][self.board_size-1-i] == player for i in range(self.board_size)):
            return True
        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_board(self):
        self.wins_losses = {"X": 0, "O": 0}
        self.current_player = "X"
        self.board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j].config(text="")
            self.start_time = 0
            self.first_move = True

    def record_high_score(self, player):
        with open("high_scores.txt", "a") as file:
            file.write(f"{player},{self.wins_losses['X']},{self.wins_losses['O']}\n")

def main_function():
    root = tk.Tk()
    name = simpledialog.askstring("Player Name", "Enter your name:")
    size = simpledialog.askinteger("Board Size", "Enter difficulty level (3 for 3x3, 4 for 4x4, etc:", initialvalue=3)
    mode = simpledialog.askstring("Mode", "Play against computer (C) or multi-player (P):", initialvalue="C").upper()
    if mode == 'P':
        second = simpledialog.askstring("Second Player", "Enter second player's name", initialvalue='Second Player')
        gui = TicTacToeGUI(root, size, mode, name, second)
    else:
        gui = TicTacToeGUI(root, size, mode, name)
    root.mainloop()

if __name__ == "__main__":
    main_function()
