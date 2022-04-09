import numpy as np
#
# '''
# 0  1  2  3  4
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44
# '''
#
# tables_values = np.empty(0)
#
# for i in range(0, 50, 10):
#     for j in range(5):
#         tables_values = np.append(tables_values, i + j)
#
# print(tables_values)
e_positions = np.array(["N", "K", "G"])
st_cor = "K"
rest_es = e_positions[e_positions != st_cor]
print(rest_es)