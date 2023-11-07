import tkinter
import tkinter.simpledialog
import tkinter.messagebox

# Initialize scores
player_x_score = 0
player_o_score = 0

# Create the game window
root = tkinter.Tk()

# Customize the game window
root.title("TicTacToe")
root.minsize(500, 500)

def check_null():
    print("check null")

def highlight_winner(combination):
    for row, col in combination:
        buttons[col][row].config(bg="yellow")

def print_winner():
    global win, player_x_score, player_o_score

    if win is False:
        win = True
        if current_player == "X":
            player_x_score += 1
            player_x_label.config(text=f"Player X: {player_x_score}")
        else:
            player_o_score += 1
            player_o_label.config(text=f"Player O: {player_o_score}")
        print("Player", current_player, "won")
        highlight_winner(winning_combination)  # Highlight the winning combination

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    player_turn_label.config(text=f"Current Turn: {current_player}")

def check_win(clicked_row, clicked_col):
    # ... (existing code for checking wins)

    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button["text"] == "X" or current_button["text"] == "O":
                    count += 1
        if count == 9:
            tkinter.messagebox.showinfo("Game Over", "It's a draw")

def place_symbol(row, column):
    print("click", row, column)
    clicked_button = buttons[column][row]
    if clicked_button["text"] == "":
        clicked_button.config(text=current_player)
        check_win(row, column)
        switch_player()

def undo_last_move():
    global previous_move
    if previous_move:
        row, column = previous_move
        buttons[column][row].config(text="")
        switch_player()  # Switch back to the previous player
        previous_move = None

def reset_game():
    global win, player_x_score, player_o_score
    win = False
    player_x_score = 0
    player_o_score = 0
    player_x_label.config(text=f"Player X: {player_x_score}")
    player_o_label.config(text=f"Player O: {player_o_score}")
    for column in range(3):
        for row in range(3):
            buttons[column][row].config(text="")
    player_turn_label.config(text="Current Turn: X")  # Reset player's turn indicator

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root,
                font=("Arial", 50),
                width=5,
                height=3,
                command=lambda r=row, c=column: place_symbol(r, c),
            )
            button.grid(row=row + 1, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# Store buttons
buttons = []
current_player = "X"
win = False
winning_combination = None
previous_move = None

# Create labels to display scores
player_x_label = tkinter.Label(root, text=f"Player X: {player_x_score}", font=("Arial", 20), fg="green")
player_x_label.grid(row=4, column=0, columnspan=3)

player_o_label = tkinter.Label(root, text=f"Player O: {player_o_score}", font=("Arial", 20), fg="blue")
player_o_label.grid(row=5, column=0, columnspan=3)

player_turn_label = tkinter.Label(root, text="Current Turn: X", font=("Arial", 20))
player_turn_label.grid(row=0, column=0, columnspan=3)

# Create a reset button
reset_button = tkinter.Button(root, text="Reset Game", font=("Arial", 20), command=reset_game)
reset_button.grid(row=6, column=0, columnspan=3)

# Create an "Undo" button
undo_button = tkinter.Button(root, text="Undo", font=("Arial", 20), command=undo_last_move)
undo_button.grid(row=7, column=0, columnspan=3)

draw_grid()
root.mainloop()
