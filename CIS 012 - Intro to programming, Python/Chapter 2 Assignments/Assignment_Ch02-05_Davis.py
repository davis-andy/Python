lDoor, wDoor = input("Enter the length and width of the door: ").split()
lWin1, wWin1 = input("Enter the length and width of the first window: ").split()
lWin2, wWin2 = input("Enter the length and width of the second window: ").split()
lBook, wBook = input("Enter the length and width of the bookshelf: ").split()
lRoom, wRoom, hRoom = input("Enter the length, width, and height of the room: ").split()
aWall1 = int(lRoom)*int(hRoom)
aWall2 = int(wRoom)*int(hRoom)
aDoor = int(lDoor)*int(wDoor)
aWin1 = int(lWin1)*int(wWin1)
aWin2 = int(lWin2)*int(wWin2)
aBook = int(lBook)*int(wBook)
aRoom = (aWall1*2)+(aWall2*2)
gal = (aRoom-aDoor-aWin1-aWin2-aBook)/120


print()
print(f"The amount of paint needed to paint the room: {gal:.2f} gallons")
