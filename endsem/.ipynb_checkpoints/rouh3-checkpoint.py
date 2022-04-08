import numpy as np
import time
from tabulate import tabulate  # pip install tabulate ( For formatting table)
from colorama import init, Fore, Back, Style  # pip install colorama ( For color highlighting)

init()


def fmt(string):
    digits = "1234567890"
    for x in string:
        if x not in digits:
            string = string.replace(x, "")
    return int(string)


def indexes(ind):
    ind = list(int(x) for x in str(ind))
    if len(ind) == 1:
        i1 = 0
        i2 = ind[0]
    else:
        i1 = ind[0]
        i2 = ind[1]
    return i1, i2


g_space = np.empty((5, 5), object)
g_space[0, 2] = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{Back.MAGENTA}-P(A)(0, 2)-{Style.RESET_ALL}"
g_space[4, 2] = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{Back.MAGENTA}-P(B)(4, 2)-{Style.RESET_ALL}"
g_space[1, 1] = f"{Style.BRIGHT}{Fore.GREEN}-E(A)(1, 1)-{Style.RESET_ALL}"
g_space[1, 4] = f"{Style.BRIGHT}{Fore.GREEN}-E(A)(1, 4)-{Style.RESET_ALL}"
g_space[3, 0] = f"{Style.BRIGHT}{Fore.RED}-E(B)(3, 0)-{Style.RESET_ALL}"
g_space[3, 3] = f"{Style.BRIGHT}{Fore.RED}-E(B)(3, 3)-{Style.RESET_ALL}"


for j in range(5):
    for k in range(5):
        if g_space[j, k] is None:
            g_space[j, k] = f"{Style.DIM}{Fore.YELLOW}-{j, k}-{Style.RESET_ALL}"

tables_values = np.empty(0)
for x in range(0, 50, 10):
    for y in range(5):
        tables_values = np.append(tables_values, x + y)

a_positions = np.array([11, 14])
b_positions = np.array([30, 33])
p_positions = np.array([2, 42])

players = ["A", "B"]
print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")
while True:
    player = players[0]
    if player == "A":
        o_positions = a_positions.copy()
        win_positions = np.array([41, 43, 32])
        electron = "E(A)"
    else:
        o_positions = b_positions.copy()
        win_positions = np.array([1, 3, 12])
        electron = "E(B)"
    e_positions = np.append(a_positions, b_positions)
    occ_positions = np.append(e_positions, p_positions)
    st_int = 55
    while st_int not in o_positions:
        while True:
            try:
                st_int = fmt(input(f"Player {player} starting coordinates(ij; i,j; i j; (i,J) etc): "))
                break
            except ValueError:
                print("Enter valid coordinates!!!")

    rest_es = list(e_positions)
    rest_es.remove(st_int)
    rest_es = np.array(rest_es)
    restricted_positions = np.empty(0)

    for i in rest_es:
        restricted_positions = np.append(restricted_positions, np.linspace(i - 1, i + 1, 3))
        restricted_positions = np.append(restricted_positions, np.linspace(i - 10, i + 10, 3))

    restricted_positions = np.append(restricted_positions, occ_positions)
    valid_moves = np.append(np.linspace(st_int - 2, st_int + 2, 5), np.linspace(st_int - 20, st_int + 20, 5))
    risk_moves = np.append(np.linspace(st_int - 2, st_int + 2, 3), np.linspace(st_int - 20, st_int + 20, 3))

    fp_int = 55
    while True:
        try:
            fp_int = fmt(input("Move to: "))
            break
        except ValueError:
            print("Illegal Move!!!")
            pass

    while True:
        if (fp_int in valid_moves) and (fp_int not in restricted_positions) and (fp_int in tables_values):
            break
        else:
            print("Illegal move!!!")
            while True:
                try:
                    fp_int = fmt(input("Move to: "))
                    break
                except ValueError:
                    print("Illegal Move!!!")
                    pass

    prob = np.random.random(1)
    if (fp_int in risk_moves) and prob <= 0.5:
        print("\nTossing the coin!")
        time.sleep(1)
        print("Bad luck, move rejected :(")
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
        print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")
    else:
        if (prob > 0.5) and (fp_int in risk_moves):
            print("\nTossing the coin!")
            time.sleep(1)
            print("Yay, move accepted :)")
        if st_int == o_positions[0]:
            o_positions[0] = fp_int
        else:
            o_positions[1] = fp_int
        for pos in o_positions:
            i1, i2 = indexes(pos)
            g_space[i1, i2] = f"{Style.BRIGHT}{Fore.RED}-{electron}{i1, i2}-{Style.RESET_ALL}"
        i1, i2 = indexes(st_int)
        g_space[i1, i2] = f"{Style.DIM}{Fore.YELLOW}-{i1, i2}-{Style.RESET_ALL}"

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
        print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")
        if fp_int in win_positions:
            print(f"Player {player} wins!!!")
            break

    players.append(player)
    players.pop(0)


'''

'''