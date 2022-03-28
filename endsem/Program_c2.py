import numpy as np

g_space = np.zeros((5, 5), object)
g_space[0, 2] = "PA"
g_space[4, 2] = "PB"
g_space[1, 1] = "EA"
g_space[1, 4] = "EA"
g_space[3, 0] = "EB"
g_space[3, 3] = "EB"

for i in range(5):
    for j in range(5):
        if g_space[i, j] == 0:
            g_space[i, j] = "--"

ae1, ae2 = 11, 14
be1, be2 = 30, 33
a_positions = np.array([ae1, ae2])
b_positions = np.array([be1, be2])
p_positions = np.array([2, 42])

players = ["A", "B"]
print(g_space)
while True:
    player = players[0]
    if player == "A":
        o_positions = a_positions.copy()
        win_positions = np.array([41, 43, 32])
        electron = "EA"
    else:
        o_positions = b_positions.copy()
        win_positions = np.array([1, 3, 12])
        electron = "EB"

    e_positions = np.append(a_positions, b_positions)
    occ_positions = np.append(e_positions, p_positions)
    st = int(input(f"Player {player} move from: "))
    while st not in o_positions:
        st = int(input("Select valid start: "))

    rest_es = list(e_positions)
    rest_es.remove(st)
    rest_es = np.array(rest_es)
    restricted_positions = np.empty(0)
    for i in rest_es:
        restricted_positions = np.append(restricted_positions, np.linspace(i - 1, i + 1, 3))
        restricted_positions = np.append(restricted_positions, np.linspace(i - 10, i + 10, 3))
    restricted_positions = np.append(restricted_positions, occ_positions)

    valid_moves = np.linspace(st - 2, st + 2, 5)
    valid_moves = np.append(valid_moves, np.linspace(st - 20, st + 20, 5))
    risk_moves = np.linspace(st - 2, st + 2, 3)
    risk_moves = np.append(risk_moves, np.linspace(st - 20, st + 20, 3))
    fp = input("Move to: ")
    while True:
        if int(fp) in valid_moves and int(fp) not in restricted_positions:
            if int(fp[0]) > 4 or int(fp[0]) < 0 or int(fp[1]) > 4 or int(fp[1]) < 0:
                print("Illegal move!!!")
                fp = int(input("Move to: "))
            else:
                break
        else:
            print("Illegal move!!!")
            fp = input("Move to: ")

    if int(fp) in risk_moves:
        prob = np.random.random(1)
        if prob > 0.5:
            print("Move rejected!")
            print(g_space)
        else:
            print("Move accepted!")
            if st == o_positions[0]:
                o_positions[0] = fp
            else:
                o_positions[1] = fp
            f_index = tuple(fp)
            i_index = tuple(str(st))
            i_index = list(map(int, i_index))
            f_index = list(map(int, f_index))
            g_space[i_index[0], i_index[1]] = "--"
            g_space[f_index[0], f_index[1]] = electron
            print(g_space)
    else:
        if st == o_positions[0]:
            o_positions[0] = fp
        else:
            o_positions[1] = fp
        f_index = tuple(fp)
        i_index = tuple(str(st))
        i_index = list(map(int, i_index))
        f_index = list(map(int, f_index))
        g_space[i_index[0], i_index[1]] = "--"
        g_space[f_index[0], f_index[1]] = electron
        print(g_space)
    if player == "A":
        a_positions = np.copy(o_positions)
    else:
        b_positions = np.copy(o_positions)
    players.append(player)
    players.pop(0)
    if int(fp) in win_positions:
        print(f"{player} wins!!!")
        break

