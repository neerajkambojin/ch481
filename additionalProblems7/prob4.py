# Binary to decimal
binum = input("Enter binary number: ")

def bitodeci(binum):
    for digit in binum:
        if int(digit) > 1:
            print("Invalid number!!!")
            break
    else:
        binum_len = len(binum)
        decinum = 0
        for i in range(binum_len):
            decinum += (pow(2, binum_len - 1 - i)) * int(binum[i])
        return (decinum)


print(f"Decimal number: {bitodeci(binum)}")
