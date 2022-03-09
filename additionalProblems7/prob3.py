import random


def fun1():
    num = random.randint(1, 6)
    if num <= 3:
        print("Hello")
    num = random.randint(1, 6)
    if num <= 2:
        print("Hi")
    num = random.randint(1, 6)
    if num == 1:
        print("Bye")


fun1()
