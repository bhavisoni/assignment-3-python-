import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Simple Ludo Game")
root.geometry("600x300")

path_length = 20  # Reduced for simplicity
players = {
    "red": {"pos": 1},    # Red starts at position 1
    "blue": {"pos": 1}    # Blue starts at position 1
}
current_player = "red"
dice_roll = 0
game_over = False

canvas = tk.Canvas(root, width=550, height=80, bg="white")
canvas.pack(pady=10)

cells = []
for i in range(path_length):
    x = 20 + i * 25
    canvas.create_rectangle(x, 20, x + 25, 45, outline="black", fill="gray" if i == 0 or i == path_length-1 else "white")
canvas.create_text(20, 60, text="Start", font=("Arial", 10))
canvas.create_text(520, 60, text="End", font=("Arial", 10))

red_piece = canvas.create_oval(15, 15, 35, 35, fill="red")
blue_piece = canvas.create_oval(15, 35, 35, 55, fill="blue")

dice_label = tk.Label(root, text="Dice: -", font=("Arial", 12))
dice_label.pack(pady=5)
status_label = tk.Label(root, text="Red's Turn", font=("Arial", 12))
status_label.pack(pady=5)

def update_board():
    for player, data in players.items():
        pos = data["pos"] - 1
        x = 20 + pos * 25
        y_offset = 0 if player == "red" else 20
        piece = red_piece if player == "red" else blue_piece
        canvas.coords(piece, x, 15 + y_offset, x + 25, 35 + y_offset)

def roll_dice():
    global dice_roll, current_player, game_over
    if game_over:
        return
    dice_roll = randint(1, 6)
    dice_label.config(text=f"Dice: {dice_roll}")
    
    new_pos = players[current_player]["pos"] + dice_roll
    if new_pos <= path_length:
        players[current_player]["pos"] = new_pos
        update_board()
        if new_pos == path_length:
            game_over = True
            status_label.config(text=f"{current_player.capitalize()} Wins!")
            return
    
    current_player = "blue" if current_player == "red" else "red"
    status_label.config(text=f"{current_player.capitalize()}'s Turn")

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 12), command=roll_dice)
roll_button.pack(pady=10)

update_board()

root.mainloop()
