a = float(input("a: "))
b = float(input("b: "))



try:
    print(a/b)
except ZeroDivisionError:
    print("Zero division not possible")
