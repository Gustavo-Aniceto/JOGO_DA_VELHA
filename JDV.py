import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_board_buttons()

    def create_board_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root, text="", font=("Helvetica", 20), width=5, height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                self.show_winner_message()
                self.reset_board()
            elif self.check_draw():
                self.show_draw_message()
                self.reset_board()
            else:
                self.toggle_player()

    def check_winner(self, row, col):
        symbol = self.current_player
        return (
            self.board[row][0] == self.board[row][1] == self.board[row][2] == symbol or
            self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol or
            self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol
        )

    def check_draw(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def toggle_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def show_winner_message(self):
        winner = "Player X" if self.current_player == "O" else "Player O"
        messagebox.showinfo("Winner", f"{winner} wins!")

    def show_draw_message(self):
        messagebox.showinfo("Draw", "It's a draw!")

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = " "
        self.current_player = "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()
