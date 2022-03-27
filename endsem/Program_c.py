import numpy as np

g_space = np.zeros((5, 5), object)
g_space[0,2] = "PA"
g_space[4, 2] = "PB"
g_space[1, 1] = "E1"
g_space[1, 4] = "E1"
g_space[3, 0] = "E2"
g_space[3, 3] = "E2"

ae1, ae2 = 11, 14
be1, be2 = 30, 33
a_positions = np.array([ae1, ae2])
b_positions = np.array([be1, be2])
p_positions = np.array([2, 42])

while True:
    x_a = int(input("Player A move from: "))
    while x_a not in a_positions:
        x_a = int(input("Select valid start: "))
    valid_moves = np.linspace(x_a - 2, x_a + 2, 5)
    vb = np.linspace(x_a - 20, x_a + 20, 5)
    valid_moves = np.append(valid_moves, vb)
    y_a = str(input("Move to: "))
    while int(y_a) not in valid_moves or int(y_a[0]) > 4 or int(y_a[0]) < 0 or int(y_a[1]) > 4 or int(y_a[1]) < 0:
        print("Invalid move!!!")
        y_a = int(input("Move to: "))
    if x_a == a_positions[0]:
        a_positions[0] = y_a
    else:
        a_positions[1] = y_a
    f_index = (tuple(str(y_a)))
    f_index = list(map(int, f_index))
    i_index = tuple(str(x_a))
    i_index = list(map(int, i_index))
    print(list(i_index))
    print(list(f_index))
    print(g_space)
    g_space[i_index[0], i_index[1]] = 0
    g_space[f_index[0], f_index[1]] = "E1"
    print(g_space)
    break









    print(a_positions)












    print("********BBBBBB************")
    print(b_positions)
    x_b = int(input("Player B move from: "))
    while x_b not in b_positions:
        x_b = int(input("Select valid start: "))
    valid_moves = np.linspace(x_b - 2, x_b + 2, 5)
    vb = np.linspace(x_b - 20, x_b + 20, 5)
    valid_moves = np.append(valid_moves, vb)
    print(valid_moves)
    y_b = int(input("Move to: "))
    while y_b not in valid_moves or int(str(y_b)[0]) > 4 or int(str(y_b)[0]) < 0 or int(str(y_b)[1]) > 4 or int(str(y_b)[1]) < 0:
        print("Invalid move!!!")
        y_b = int(input("Move to: "))
    if x_b == b_positions[0]:
        b_positions[0] = y_b
    else:
        b_positions[1] = y_b
    print(b_positions)
    exit()



# invalid_moves = a_positions.copy()
#     invalid_moves = np.append(invalid_moves, p_positions)
#     invalid_moves = np.append(invalid_moves, a_positions + 11)
#     invalid_moves = np.append(invalid_moves, a_positions - 11)
#     invalid_moves = np.append(invalid_moves, a_positions - 9)
#     invalid_moves = np.append(invalid_moves, a_positions + 9)
