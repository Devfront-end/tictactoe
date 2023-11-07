import tkinter

def check_win(clicked_row, clicked_col):
    # détecter victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        #current_button.config(text="Check")
        if current_button["text"] == "X":
            count += 1
            if count == 3:
                print("Player 1 wins horizontally")

    # détecter victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        if current_button["text"] == "X":
            count += 1
            if count == 3:
                print("Player 1 wins vertically")

    # détecter victoire diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button["text"] == "X":
            count += 1
            if count == 3:
                print("Player 1 wins in diagonal")
    
    # détecter victoire diagonale inversée
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button["text"] == "X":
            count += 1
            if count == 3:
                print("Player 1 wins in diagonal")

# Define buttons list here
buttons = []

def place_symbol(row, column):
    print("click", row, column)
    # place the symbol in the button
    clicked_button = buttons[column][row]
    clicked_button.config(text="X")
    # check if the player has won
    check_win(row, column)  # Call the check_win function

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# créer la fenêtre du jeu
root = tkinter.Tk()

# personnalisation de la fenêtre du jeu
root.title("TicTacToe")
root.minsize(500, 500)
draw_grid()
root.mainloop()
