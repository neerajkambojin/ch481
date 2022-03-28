import numpy as np
from tabulate import tabulate

g_space = np.empty((5, 5), object)
g_space[0, 2] = "P(A)"
g_space[4, 2] = "P(B)"
g_space[1, 1] = "E(A)"
g_space[1, 4] = "E(A)"
g_space[3, 0] = "E(B)"
g_space[3, 3] = "E(B)"

for i in range(5):
    for j in range(5):
        if g_space[i, j] is None:
            g_space[i, j] = "--"


a_positions = np.array([11, 14])
b_positions = np.array([30, 33])
p_positions = np.array([2, 42])

players = ["A", "B"]
print(f"\nTable: \n{tabulate(g_space, tablefmt='grid')}\n")
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
    st_str = input(f"Player {player} starting coordinates (e.g. 11, 14 etc): ")
    st_int = int(st_str)
    while st_int not in o_positions:
        st_str = input("Select valid coordinates: ")
        st_int = int(st_str)

    rest_es = list(e_positions)
    rest_es.remove(st_int)
    rest_es = np.array(rest_es)
    restricted_positions = np.empty(0)
    for i in rest_es:
        restricted_positions = np.append(restricted_positions, np.linspace(i - 1, i + 1, 3))
        restricted_positions = np.append(restricted_positions, np.linspace(i - 10, i + 10, 3))
    restricted_positions = np.append(restricted_positions, occ_positions)

    valid_moves = np.linspace(st_int - 2, st_int + 2, 5)
    valid_moves = np.append(valid_moves, np.linspace(st_int - 20, st_int + 20, 5))
    risk_moves = np.linspace(st_int - 2, st_int + 2, 3)
    risk_moves = np.append(risk_moves, np.linspace(st_int - 20, st_int + 20, 3))
    fp = input("Move to: ")
    while True:
        if int(fp) in valid_moves and int(fp) not in restricted_positions and len(fp) == 2:
            if int(fp[0]) > 4 or int(fp[0]) < 0 or int(fp[1]) > 4 or int(fp[1]) < 0:
                print("Illegal move!!!")
                fp = int(input("Move to: "))
            else:
                break
        else:
            print("Illegal move!!!")
            fp = input("Move to: ")
    prob = np.random.random(1)
    if (int(fp) in risk_moves) and prob >= 0.5:
        print("\nMove rejected!")
        print(f"\nTable: \n{tabulate(g_space, tablefmt='grid')}\n")
    else:
        if (prob < 0.5) and (int(fp) in risk_moves):
            print("\nMove accepted!")
        if st_int == o_positions[0]:
            o_positions[0] = fp
        else:
            o_positions[1] = fp
        i_index = tuple(str(st_str))
        f_index = tuple(str(fp))
        i_index = list(map(int, i_index))
        f_index = list(map(int, f_index))
        g_space[i_index[0], i_index[1]] = "--"
        g_space[f_index[0], f_index[1]] = electron
        print(f"\nTable: \n{tabulate(g_space, tablefmt='grid')}\n")
    if player == "A":
        a_positions = np.copy(o_positions)
    else:
        b_positions = np.copy(o_positions)
    players.append(player)
    players.pop(0)
    if int(fp) in win_positions:
        print(f"Player {player} wins!!!")
        break
