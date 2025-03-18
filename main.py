import tkinter as tk
import random

board = {2: 38, 8: 31, 16: 6, 21: 42, 28: 84, 36: 44, 46: 25, 49: 11,
         51: 67, 62: 19, 64: 60, 71: 91, 74: 53, 78: 98, 87: 94, 89: 68,
         92: 88, 95: 75, 99: 80}


def roll_dice():
    return random.randint(1, 6)


def move_player(player):
    dice = roll_dice()

    if player["position"] == 0:
        if dice == 6:
            player["position"] = 1
    else:
        new_position = player["position"] + dice

        if new_position in board:
            new_position = board[new_position]

        if new_position <= 100:
            player["position"] = new_position

    return dice


def update_board():
    canvas.delete("all")
    draw_board()
    draw_snakes_and_ladders()
    for player in players:
        x, y = get_coordinates(player["position"])
        canvas.create_oval(x, y, x + 20, y + 20, fill=player["color"], outline="black", width=2)


def draw_board():
    colors = ["#F4A100", "#FCE181"]  # Dark yellow and light yellow
    for i in range(10):
        for j in range(10):
            x1, y1 = j * 40, (9 - i) * 40
            x2, y2 = x1 + 40, y1 + 40
            num = i * 10 + j + 1 if i % 2 == 0 else (i * 10) + 10 - j
            color = colors[(i + j) % 2]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(num), font=("Arial", 10, "bold"), fill="black")


def draw_snakes_and_ladders():
    for start, end in board.items():
        x1, y1 = get_coordinates(start)
        x2, y2 = get_coordinates(end)
        color = "red" if start > end else "green"
        width = 3 if start > end else 5
        canvas.create_line(x1 + 8, y1 + 8, x2 + 8, y2 + 8, fill=color, width=width, arrow=tk.LAST)


def get_coordinates(position):
    if position == 0:
        return -100, -100
    row = (position - 1) // 10
    col = (position - 1) % 10
    if row % 2 == 0:
        x = col * 40
    else:
        x = (9 - col) * 40
    y = (9 - row) * 40
    return x + 8, y + 8


def next_turn():
    global current_player_index
    player = players[current_player_index]
    dice = move_player(player)
    update_board()

    if player["position"] == 100:
        message.set(f"{player['name']} wins! 🎉")
        roll_button.config(state=tk.DISABLED)
    else:
        if player["position"] == 0:
            message.set(f"{player['name']} rolled a {dice}. Need a 6 to enter the board.")
        else:
            message.set(f"{player['name']} rolled a {dice} and moved to square {player['position']}")

        current_player_index = (current_player_index + 1) % len(players)


def start_game():
    global players, current_player_index, message, roll_button
    players = []
    colors = ["red", "green", "blue", "yellow"]

    for i in range(4):
        name = player_entries[i].get().strip()
        if name:
            players.append({"name": name, "position": 0, "color": colors[i]})

    if not players:
        return

    update_board()
    current_player_index = 0
    message.set(f"{players[0]['name']}'s turn. Press 'Roll Dice' to start.")

    for entry in player_entries:
        entry.config(state=tk.DISABLED)

    roll_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Snakes and Ladders")
root.configure(bg="#ADD8E6")

canvas = tk.Canvas(root, width=400, height=400, bg="#FFFFFF")
canvas.pack(pady=10)
draw_board()

player_entries = []
for i in range(4):
    tk.Label(root, text=f"Player {i + 1} Name:", font=("Arial", 12), bg="#ADD8E6").pack()
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack()
    player_entries.append(entry)

start_button = tk.Button(root, text="Start Game", font=("Arial", 14, "bold"), command=start_game, bg="#4CAF50",
                         fg="white")
start_button.pack(pady=5)

message = tk.StringVar()
message_label = tk.Label(root, textvariable=message, font=("Arial", 12, "bold"), bg="#ADD8E6", fg="black")
message_label.pack(pady=5)

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14, "bold"), state=tk.DISABLED, command=next_turn,
                        bg="#FF5733", fg="white")
roll_button.pack(pady=5)

root.mainloop()