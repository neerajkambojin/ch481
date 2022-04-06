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

while True:
    print("*********AAA*********")
    e_positions = np.append(a_positions, b_positions)
    occ_positions = np.append(e_positions, p_positions)
    print(g_space)
    x_a = int(input("Player A move from: "))
    while x_a not in a_positions:
        x_a = int(input("Select valid start: "))

    rest_es = list(e_positions)
    rest_es.remove(x_a)
    rest_es = np.array(rest_es)
    restricted_positions = np.empty(0)
    for i in rest_es:
        restricted_positions = np.append(restricted_positions, np.linspace(i - 1, i + 1, 3))
        restricted_positions = np.append(restricted_positions, np.linspace(i - 10, i + 10, 3))
    restricted_positions = np.append(restricted_positions, occ_positions)

    valid_moves = np.linspace(x_a - 2, x_a + 2, 5)
    valid_moves = np.append(valid_moves, np.linspace(x_a - 20, x_a + 20, 5))
    risk_moves = np.linspace(x_a - 2, x_a + 2, 3)
    risk_moves = np.append(risk_moves, np.linspace(x_a - 20, x_a + 20, 3))
    win_positions = np.array([41, 43, 32])
    y_a = input("Move to: ")
    while True:
        if int(y_a) in valid_moves and int(y_a) not in restricted_positions:
            if int(y_a[0]) > 4 or int(y_a[0]) < 0 or int(y_a[1]) > 4 or int(y_a[1]) < 0:
                print("Illegal move!!!")
                y_a = int(input("Move to: "))
            else:
                break
        else:
            print("Illegal move!!!")
            y_a = input("Move to: ")

    if int(y_a) in risk_moves:
        prob = np.random.random(1)
        if prob > 0.5:
            print("Move rejected!")
            print(g_space)
        else:
            print("Move accepted!")
            if x_a == a_positions[0]:
                a_positions[0] = y_a
            else:
                a_positions[1] = y_a
            f_index = tuple(y_a)
            i_index = tuple(str(x_a))
            i_index = list(map(int, i_index))
            f_index = list(map(int, f_index))
            g_space[i_index[0], i_index[1]] = "--"
            g_space[f_index[0], f_index[1]] = "EA"
            print(g_space)
    else:
        if x_a == a_positions[0]:
            a_positions[0] = y_a
        else:
            a_positions[1] = y_a
        f_index = tuple(y_a)
        i_index = tuple(str(x_a))
        i_index = list(map(int, i_index))
        f_index = list(map(int, f_index))
        g_space[i_index[0], i_index[1]] = "--"
        g_space[f_index[0], f_index[1]] = "EA"
        print(g_space)
    if int(y_a) in win_positions:
        print("A wins!!!")
        break


    e_positions = np.append(a_positions, b_positions)
    occ_positions = np.append(e_positions, p_positions)
    x_b = int(input("Player B move from: "))
    while x_b not in b_positions:
        x_b = int(input("Select valid start: "))

    rest_es = list(e_positions)
    rest_es.remove(x_b)
    rest_es = np.array(rest_es)
    restricted_positions = np.empty(0)
    for i in rest_es:
        restricted_positions = np.append(restricted_positions, np.linspace(i - 1, i + 1, 3))
        restricted_positions = np.append(restricted_positions, np.linspace(i - 10, i + 10, 3))
    restricted_positions = np.append(restricted_positions, occ_positions)

    valid_moves = np.linspace(x_b - 2, x_b + 2, 5)
    valid_moves = np.append(valid_moves, np.linspace(x_b - 20, x_b + 20, 5))
    risk_moves = np.linspace(x_b - 2, x_b + 2, 3)
    risk_moves = np.append(risk_moves, np.linspace(x_b - 20, x_b + 20, 3))
    win_positions = np.array([1, 3, 12])
    y_b = input("Move to: ")
    while True:
        if int(y_b) in valid_moves and int(y_b) not in restricted_positions:
            if int(y_b[0]) > 4 or int(y_b[0]) < 0 or int(y_b[1]) > 4 or int(y_b[1]) < 0:
                print("Illegal move!!!")
                y_b = int(input("Move to: "))
            else:
                break
        else:
            print("Illegal move!!!")
            y_b = input("Move to: ")

    if int(y_b) in risk_moves:
        prob = np.random.random(1)
        if prob > 0.5:
            print("Move rejected!")
            print(g_space)
        else:
            print("Move accepted!")
            if x_b == a_positions[0]:
                a_positions[0] = y_b
            else:
                a_positions[1] = y_b
            f_index = tuple(y_b)
            i_index = tuple(str(x_b))
            i_index = list(map(int, i_index))
            f_index = list(map(int, f_index))
            g_space[i_index[0], i_index[1]] = "--"
            g_space[f_index[0], f_index[1]] = "EB"
            print(g_space)
    else:
        if x_b == b_positions[0]:
            b_positions[0] = y_b
        else:
            b_positions[1] = y_b
        f_index = tuple(y_b)
        i_index = tuple(str(x_b))
        i_index = list(map(int, i_index))
        f_index = list(map(int, f_index))
        g_space[i_index[0], i_index[1]] = "--"
        g_space[f_index[0], f_index[1]] = "EB"
        print(g_space)
    if int(y_b) in win_positions:
        print("B wins!!!")
        break


'''
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
g_space[0, 2] = "P(A)"
g_space[4, 2] = "P(B)"
g_space[1, 1] = "E(A)"
g_space[1, 4] = "E(A)"
g_space[3, 0] = "E(B)"
g_space[3, 3] = "E(B)"

for j in range(5):
    for k in range(5):
        if g_space[j, k] is None:
            g_space[j, k] = f"--"

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
        g_space[i_index[0], i_index[1]] = f"--"
        g_space[f_index[0], f_index[1]] = electron
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

'''

'''

'''