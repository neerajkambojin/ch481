# To assign grades

marks = float(input("Enter marks: "))
while marks > 100:
    marks = float(input("Enter valid marks: "))
if 100 >= marks >= 95:
    print("AP")
elif 95 > marks >= 85:
    print("AA")
elif 85 > marks >= 75:
    print("AB")
elif 75 > marks >= 65:
    print("BB")
else:
    print("Tu to gya!!! Khtm tata bye bye")