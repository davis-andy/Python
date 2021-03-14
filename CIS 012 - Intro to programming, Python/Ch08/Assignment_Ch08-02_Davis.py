tableSize = 11 #table size = number + 1
startList = 0
row = 0
column = 0
list1D = 0
list2D = 0
flag = True
MT = []

print("Multiplication Table:")
while flag == True:
    while startList < tableSize:
        MT.append([0]*tableSize)
        startList+=1
    while row < tableSize:
        if row == 0:
            while column < tableSize:
                if column == 0:
                    MT[row][column] = "X"
                    column += 1
                else:
                    MT[row][column] = column
                    column += 1
            row += 1
        else:
            column = 0
            while column < tableSize:
                if column == 0:
                    MT[row][column] = row
                    column += 1
                else:
                    MT[row][column] = row * column
                    column += 1
            row += 1
    while list1D < tableSize:
        list2D = 0
        while list2D < tableSize:
            if list2D == (tableSize-1):
                print(MT[list1D][list2D], end = "\n")
                list2D += 1
            else:
                print(MT[list1D][list2D], end = "\t")
                list2D += 1
        list1D += 1
    flag = False
