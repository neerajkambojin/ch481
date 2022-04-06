import numpy as np
import time
from tabulate import tabulate   # pip install tabulate


def formatter(string):
    digits = "1234567890"
    for x in string:
        if x not in digits:
            string = string.replace(x, "")
    return string


g_space = np.empty((5, 5), object)
g_space[0, 2] = "-P(A)-\n(0, 2)"
g_space[4, 2] = "-P(B)-\n(4, 2)"
g_space[1, 1] = "-E(A)-\n(1, 1)"
g_space[1, 4] = "-E(A)-\n(1, 4)"
g_space[3, 0] = "-E(B)-\n(3, 0)"
g_space[3, 3] = "-E(B)-\n(3, 3)"

for j in range(5):
    for k in range(5):
        if g_space[j, k] is None:
            g_space[j, k] = f"------\n{j, k}"

a_positions = np.array([11, 14])
b_positions = np.array([30, 33])
p_positions = np.array([2, 42])

players = ["A", "B"]
print(f"\nTable: \n{tabulate(g_space, tablefmt = 'fancy_grid')}\n")
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

    while True:
        try:
            st_str = formatter(input(
                f"Player {player} starting coordinates (Valid input format e.g. 14, (1,4), 1 4, '1, 4'): "))
            st_int = int(st_str)
            break
        except ValueError:
            print("Enter valid coordinates!!!")
            pass

    while st_int not in o_positions:
        print("Enter valid coordinates!!!")
        while True:
            try:
                st_str = formatter(input(
                    f"Player {player} starting coordinates (Valid input format e.g. 14, (1,4), 1 4, '1, 4'): "))
                st_int = int(st_str)
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

    while True:
        try:
            fp_str = formatter(input("Move to: "))
            fp_int = int(fp_str)
            break
        except ValueError:
            print("Illegal Move!!!")
            pass

    while True:
        if fp_int in valid_moves and fp_int not in restricted_positions and len(fp_str) == 2:
            if int(fp_str[0]) > 4 or int(fp_str[0]) < 0 or int(fp_str[1]) > 4 or int(fp_str[1]) < 0:
                print("Illegal move!!!")
                while True:
                    try:
                        fp_str = formatter(input("Move to: "))
                        fp_int = int(fp_str)
                        break
                    except ValueError:
                        print("Illegal Move!!!")
                        pass
            else:
                break
        else:
            print("Illegal move!!!")
            while True:
                try:
                    fp_str = formatter(input("Move to: "))
                    fp_int = int(fp_str)
                    break
                except ValueError:
                    print("Illegal Move!!!")
                    pass

    prob = np.random.random(1)
    if (fp_int in risk_moves) and prob >= 0.5:
        print("\nTossing the coin!")
        time.sleep(1)
        print("Bad luck, move rejected :(")
        print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")
    else:
        if (prob < 0.5) and (fp_int in risk_moves):
            print("\nTossing the coin!")
            time.sleep(1)
            print("Yay, move accepted :)")
        if st_int == o_positions[0]:
            o_positions[0] = fp_str
        else:
            o_positions[1] = fp_str
        i_index = tuple(st_str)
        f_index = tuple(fp_str)
        i_index = list(map(int, i_index))
        f_index = list(map(int, f_index))
        g_space[i_index[0], i_index[1]] = f"  ------\n{i_index[0], i_index[1]}"
        g_space[f_index[0], f_index[1]] = f"-{electron}-\n{f_index[0], f_index[1]}"
        print(f"\nTable: \n{tabulate(g_space, tablefmt='fancy_grid')}\n")
        if fp_int in win_positions:
            print(f"Player {player} wins!!!")
            break

    if player == "A":
        a_positions = np.copy(o_positions)
    else:
        b_positions = np.copy(o_positions)

    players.append(player)
    players.pop(0)
