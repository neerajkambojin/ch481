f_v = [(3, 7), (4, 10), (2, 9), (-4, 200), (50, 60), (8, 20)]


def m_value(f_v):
    for data in f_v:
        if data[1] == max(i[1] for i in f_v):
            print(data[0])


m_value(f_v)
