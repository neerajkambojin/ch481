# number = int(input("Number: "))
# while True:
#     print(number % 10)
#     number = number // 10
#     if number//10 == 0:
#         print(number)
#         break

sum = 0
number = input("Number: ")
length = len(number)
for i in number:
    sum += int(i)**length
if int(number) == sum:
    print("Yes")
else:
    print("No")