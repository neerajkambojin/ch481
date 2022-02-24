def value(i):
    def fun(i):
        if i%2 == 0:
            return i
        else:
            return 2*i
    if i == 1:
        return 2
    else:
        val = fun(i) + 1/(value(i-1))
        return val


print(value(10))