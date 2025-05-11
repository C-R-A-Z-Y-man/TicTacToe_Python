import tkinter as tk

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe - XOX")
root.geometry("300x370")
root.resizable(False, False)

# Variables
current_player = "X"
board = [""] * 9
buttons = []

# Function to check winner
def check_winner():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Tie"
    return None

# Function when cell is clicked
def cell_clicked(i):
    global current_player
    if board[i] == "":
        board[i] = current_player
        buttons[i]["text"] = current_player
        buttons[i]["fg"] = "blue" if current_player == "X" else "red"
        winner = check_winner()
        if winner:
            result = f"Winner: {winner}" if winner != "Tie" else "It's a Tie!"
            status_label.config(text=result)
            for b in buttons:
                b.config(state="disabled")
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"{current_player}'s Turn")

# Function to restart the game
def restart_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for b in buttons:
        b.config(text="", state="normal", fg="black")
    status_label.config(text="X's Turn")

# Create grid buttons
for i in range(9):
    b = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                  command=lambda i=i: cell_clicked(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

# Status label
status_label = tk.Label(root, text="X's Turn", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3, pady=5)

# Restart button
restart_btn = tk.Button(root, text="Restart", font=("Arial", 12), bg="lightgray", command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

# Run the app
root.mainloop()
