"""

The Numera Game:
Player to reach 11 first will win.

"""

players = ["B", "A"]
player = "B"
count = 1

while count < 11:
    while True:
        print(f"Current count: {count}")
        try:
            inp = int(input(f"Player {player} enter the number: "))
            break
        except ValueError:
            print("Invalid input")
            pass
    while inp > count + 3 or inp <= count:
        print("Invalid input")
        while True:
            print(f"Current count: {count}")
            try:
                inp = int(input(f"Player {player} enter the number: "))
                break
            except ValueError:
                print("Invalid input")
                pass
    count = inp
    players.append(player)
    players.pop(0)
    player = players[0]

else:
    print(f"Current count: {count}")
    print(f"Player {players[1]} wins!!!")
