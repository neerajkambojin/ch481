# The Numera game
i = 1 # Game started by player A with 1

print("Game started by player A with 1")

while i < 11: # Condition for game

# To avoid float/string etc
    try:
        print(f"Count: {i}")
        player_b = int(input("Player B enter the number: "))

    except ValueError:
        print(f"Count: {i}")
        player_b = int(input("Enter only Integer(B): "))

# To allow natural numbers till 3 only:
    while player_b > 3 or 0 >= player_b:
        print(f"Count: {i}")
        try:
            player_b = int(input("Please enter a number greater than zero but not greater than 3(B): "))
        except ValueError:
            player_b = int(input("Enter only Integer(B): "))
    i+= player_b # Adding to total count
    print(f"Count: {i}")

    if i >= 11:  # Checking if Player B has won
        print("Player B wins!!!")
        print(f"Count: {i}")
        break
    else:
        try:            # To avoid float/string etc
            player_a = int(input("Player A enter the number: "))
        except ValueError:
            print(f"Count: {i}")
            player_a = int(input("Enter only Integer(A): "))

# To allow natural numbers till 3 only:
        while player_a > 3 or 0 >= player_a:
            print(f"Count: {i}")
            try:
                player_a = int(input("Please enter a number greater than zero but not greater than 3(A): "))
            except ValueError:
                player_a = int(input("Enter only Integer(A): "))
        i+=player_a

    if i >= 11: # Checking if Player A has won
        print("Player A wins!!!")
        print(f"Count: {i}")

#Yhi h jo h!