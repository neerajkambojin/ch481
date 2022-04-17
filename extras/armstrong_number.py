

sum = 0
number = input("Number: ")
length = len(number)
for i in number:
    sum += int(i)**length
if int(number) == sum:
    print("Yes")
else:
    print("No")