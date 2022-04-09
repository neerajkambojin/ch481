import numpy as np
import time
from tabulate import tabulate  # pip install tabulate ( For formatting table)
from colorama import init, Fore, Back, Style  # pip install colorama ( For color highlighting)


# Filtering out undesired elements from input
def fmt(string):
    digits = "1234567890"
    for x in string:
        if x not in digits:
            string = string.replace(x, "")
    return int(string)


# Coordinate to index
def indexes(ind):
    ind = list(int(x) for x in str(ind))
    if len(ind) == 1:
        i1 = 0
        i2 = ind[0]
    else:
        i1 = ind[0]
        i2 = ind[1]
    return i1, i2


init()  # Initializing colorama

# Generating board and assigning starting positions to electrons and protons
g_space = np.empty((5, 5), object)
g_space[0, 2] = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{Back.MAGENTA}-P(A)(0, 2)-{Style.RESET_ALL}"
g_space[4, 2] = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{Back.MAGENTA}-P(B)(4, 2)-{Style.RESET_ALL}"
g_space[1, 1] = f"{Style.BRIGHT}{Fore.GREEN}-E(A)(1, 1)-{Style.RESET_ALL}"
g_space[1, 4] = f"{Style.BRIGHT}{Fore.GREEN}-E(A)(1, 4)-{Style.RESET_ALL}"
g_space[3, 0] = f"{Style.BRIGHT}{Fore.RED}-E(B)(3, 0)-{Style.RESET_ALL}"
g_space[3, 3] = f"{Style.BRIGHT}{Fore.RED}-E(B)(3, 3)-{Style.RESET_ALL}"

# Filling empty positions
for j in range(5):
    for k in range(5):
        if g_space[j, k] is None:
            g_space[j, k] = f"{Style.DIM}{Fore.YELLOW}-{j, k}-{Style.RESET_ALL}"

# Generating array containing all coordinates of board
tables_values = np.empty(0)
for x in range(0, 50, 10):
    for y in range(5):
        tables_values = np.append(tables_values, x + y)

# Making list containing initial positions of electrons and protons
a_positions = np.array([11, 14])
b_positions = np.array([30, 33])
p_positions = np.array([2, 42])

# Players list for use in switching players
players = ["A", "B"]
print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")

# Starting main loop
while True:
    player = players[0]  # Selecting player
    if player == "A":
        o_positions = a_positions.copy()
        win_positions = np.array([41, 43, 32])
        electron = "E(A)"
    else:
        o_positions = b_positions.copy()
        win_positions = np.array([1, 3, 12])
        electron = "E(B)"
    e_positions = np.append(a_positions, b_positions)  # electron positions
    occ_positions = np.append(e_positions, p_positions)  # all occupied positions
    st_cor = 55  # Initializing starting coordinates variable
    while st_cor not in o_positions:  # checking if electron coordinate is valid
        while True:
            try:  # try except condition to avoid crashing due to ValueError
                st_cor = fmt(input(f"Player {player} starting coordinates(ij; i,j; i j; (i,J) etc): "))
                break
            except ValueError:
                print("Enter valid coordinates!!!")

    rest_es = e_positions[e_positions != st_cor]  # electrons except the selected one

    # generating array of positions next to electrons
    restricted_positions = np.empty(0).astype(int)
    for i in rest_es:
        restricted_positions = np.append(restricted_positions, np.linspace(i - 1, i + 1, 3))
        restricted_positions = np.append(restricted_positions, np.linspace(i - 10, i + 10, 3))

    # array containing forbidden positions
    restricted_positions = np.append(restricted_positions, occ_positions)

    # array for valid moves
    valid_moves = np.append(np.linspace(st_cor - 2, st_cor + 2, 5), np.linspace(st_cor - 20, st_cor + 20, 5)).astype(int)
    # array for moves with step = +-2
    risk_moves = np.append(np.linspace(st_cor - 2, st_cor + 2, 3), np.linspace(st_cor - 20, st_cor + 20, 3)).astype(int)

    # highlighting allowed moves
    for pos in valid_moves:
        if pos in risk_moves:
            if (pos in tables_values) and (pos not in restricted_positions):
                i1, i2 = indexes(pos)
                g_space[i1, i2] = f"{Style.BRIGHT}{Fore.MAGENTA}-{i1, i2}-{Style.RESET_ALL}"
        else:
            if (pos in tables_values) and (pos not in restricted_positions):
                i1, i2 = indexes(pos)
                g_space[i1, i2] = f"{Style.BRIGHT}{Fore.CYAN}-{i1, i2}-{Style.RESET_ALL}"
    print(tabulate(g_space, tablefmt='fancy_grid'))

    while True:
        try:
            f_cor = fmt(input("Move to: "))
            break
        except ValueError:
            print("Illegal Move!!!")
            pass

    while True:
        # condition to avoid invalid move
        if (f_cor in valid_moves) and (f_cor not in restricted_positions) and (f_cor in tables_values):
            break
        else:
            print("Illegal move!!!")
            while True:
                try:
                    f_cor = fmt(input("Move to: "))
                    break
                except ValueError:
                    print("Illegal Move!!!")
                    pass

    prob = np.random.random(1)  # for probability
    if (f_cor in risk_moves) and prob <= 0.5:  # for forbidden move
        print("\nTossing the coin!")
        time.sleep(1)
        print("Bad luck, move rejected :(")

        # changing colors
        for pos in o_positions:
            i1, i2 = indexes(pos)
            g_space[i1, i2] = f"{Style.BRIGHT}{Fore.RED}-{electron}{i1, i2}-{Style.RESET_ALL}"
        if player == "A":
            for pos in b_positions:
                i1, i2 = indexes(pos)
                g_space[i1, i2] = f"{Style.BRIGHT}{Fore.GREEN}-E(B){i1, i2}-{Style.RESET_ALL}"
        else:
            for pos in a_positions:
                i1, i2 = indexes(pos)
                g_space[i1, i2] = f"{Style.BRIGHT}{Fore.GREEN}-E(A){i1, i2}-{Style.RESET_ALL}"
    else:
        if (prob > 0.5) and (f_cor in risk_moves):  # for allowed move
            print("\nTossing the coin!")
            time.sleep(1)
            print("Yay, move accepted :)")
        if st_cor == o_positions[0]:
            o_positions[0] = f_cor
        else:
            o_positions[1] = f_cor

        # moving electron
        for pos in o_positions:
            i1, i2 = indexes(pos)
            g_space[i1, i2] = f"{Style.BRIGHT}{Fore.RED}-{electron}{i1, i2}-{Style.RESET_ALL}"
        i1, i2 = indexes(st_cor)
        g_space[i1, i2] = f"{Style.DIM}{Fore.YELLOW}-{i1, i2}-{Style.RESET_ALL}"

        # changing colors
        if player == "A":
            a_positions = np.copy(o_positions)
            for pos in b_positions:
                i1, i2 = indexes(pos)
                g_space[i1, i2] = f"{Style.BRIGHT}{Fore.GREEN}-E(B){i1, i2}-{Style.RESET_ALL}"
        else:
            b_positions = np.copy(o_positions)
            for pos in a_positions:
                i1, i2 = indexes(pos)
                g_space[i1, i2] = f"{Style.BRIGHT}{Fore.GREEN}-E(A){i1, i2}-{Style.RESET_ALL}"

        # condition for winning
        if f_cor in win_positions:
            print(f"Player {player} wins!!!")
            break

    e_positions = np.append(a_positions, b_positions)
    occ_positions = np.append(e_positions, p_positions)

    # resetting colors of unoccupied positions
    for j in range(5):
        for k in range(5):
            if (10 * j) + k not in occ_positions:
                g_space[j, k] = f"{Style.DIM}{Fore.YELLOW}-{j, k}-{Style.RESET_ALL}"
    print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")
    # changing player
    players.append(player)
    players.pop(0)
