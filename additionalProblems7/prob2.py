def fun(ls):
    ls_set = set(ls)
    for i in ls_set:
        count = 0
        for j in ls:
            if j == i:
                count += 1
        print(f"Integer: {i}, Frequency: {count}")


fun([2, 4, 7, 2, 3, 9, 12, 6, 2, 4, 8, 34, 14, 5, 7, 3])
