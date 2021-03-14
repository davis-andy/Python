p1 = input("Enter [R]ock, [P]aper, or [S]cissors\nPlayer 1: ").lower()
p2 = input("Enter [R]ock, [P]aper, or [S]cissors\nPlayer 2: ").lower()

if p1 == "r":
    if p2 == "r":
        print()
        print("Nobody WINS!")
    elif p2 == "p":
        print()
        print("Paper covers rock,\nPlayer 2 WINS!")
    elif p2 == "s":
        print()
        print("Rock smashes scissors,\nPlayer 1 WINS!")
elif p1 == "p":
    if p2 == "p":
        print()
        print("Nobody WINS!")
    elif p2 == "r":
        print()
        print("Paper covers rock,\nPlayer 1 WINS!")
    elif p2 == "s":
        print()
        print("Scissors cuts paper,\nPlayer 2 WINS!")
elif p1 == "s":
    if p2 == "s":
        print()
        print("Nobody WINS!")
    elif p2 == "p":
        print()
        print("Scissors cuts paper,\nPlayer 1 WINS!")
    elif p2 == "r":
        print()
        print("Rock smashes scissors,\nPlayer 2 WINS!")
