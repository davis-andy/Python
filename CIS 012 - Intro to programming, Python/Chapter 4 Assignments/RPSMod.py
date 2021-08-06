import random

def collectStringInput():
    p1 = input("Enter [R]ock, [P]aper, or [S]cissors\nPlayer: ").lower()
    return p1

def generateIntegerValue():
    comp = random.randint(1,3)
    return comp

def convertIntegerToRPS(convert):
    if convert == 1:
        return "r"
    elif convert == 2:
        return "p"
    elif convert == 3:
        return "s"

def evaluateWinning(play1, compute):
    if play1 == "r":
        if compute == "r":
            print("Tie!")
        elif compute == "p":
            print("Paper covers rock,\nComputer WINS!")
        elif compute == "s":
            print("Rock smashes scissors,\nPlayer WINS!")
    elif play1 == "p":
        if compute == "p":
            print("Tie!")
        elif compute == "r":
            print("Paper covers rock,\nPlayer WINS!")
        elif compute == "s":
            print("Scissors cuts paper,\nComputer WINS!")
    elif play1 == "s":
        if compute == "s":
            print("Tie!")
        elif compute == "p":
            print("Scissors cuts paper,\nPlayer WINS!")
        elif compute == "r":
            print("Rock smashes scissors,\nComputer WINS!")
