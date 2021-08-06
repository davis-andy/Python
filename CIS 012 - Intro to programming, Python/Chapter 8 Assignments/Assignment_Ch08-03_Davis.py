inStock = [] #2D list with 10 rows, 4 columns
alpha = [] #1D list with 20 elements
beta = [] #1D list with 20 elements
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

def setZero():
    #initializes any 1D list to 0 (alpha and beta)
    for _ in range(20):
        alpha.append(0)
        beta.append(0)


def inputArray():
    #prompts the user to input 20 numbers and stores the numbers into alpha
    global alpha
    print("Enter 20 integers:")
    alpha = [int(input("")) for i in range(20)]
    print()


def doubleArray():
    #initializes the elements of beta to two times the corresponding elements in alpha
    global beta
    for item in range(len(alpha)):
         beta[item] = alpha[item] * 2


def copyGamma():
    #sets the elements of the first row of inStock from gamma and the remaining rows of inStock to three times the previous row of inStock
    global inStock
    inStock = [gamma]*10

    for i in range(len(inStock)):
        if i == 0:
            for j in range(len(inStock[i])):
                if j == 3:
                    print(inStock[i][j], end = "\n")
                else:
                    print(inStock[i][j], end = "\t")
        else:
            for j in range(len(inStock[i])):
                inStock[i][j] = inStock[i-1][j] * 3
                if j == 3:
                    print(inStock[i][j], end = "\n")
                else:
                    print(inStock[i][j], end = "\t")
    print()


def copyAlphaBeta():
    #stores alpha into the first first five rows of inStock and beta into the last five rows of inStock
    global inStock
    inStock = [alpha[:4], alpha[4:8], alpha[8:12], alpha[12:16], alpha[16:], beta[:4], beta[4:8], beta[8:12], beta[12:16], beta[16:]]

    for i in range(len(inStock)):
        for j in range(len(inStock[i])):
            if j == 3:
                print(inStock[i][j], end = "\n")
            else:
                print(inStock[i][j], end = "\t")
    print()



def printArray(list1D):
    #prints any 1D list.
    #The function must contain only one loop to print any 1D list
    for i in range(len(list1D)):
        if not i == 9:
            print(list1D[i], end = "\t")
        else:
            print(list1D[i], end = "\n")
    print("\n")



def setInStock():
    #prompts the user to input the elements from the first column of inStock.
    #The function should then set the elements in the remaining columns to two times the corresponding element in the previous column, minus the corresponding element in delta.
    global inStock
    inStock = []
    print("Enter 10 integers:")
    set = [int(input("")) for i in range(10)]
    for user in set:
        inStock.extend([[user]*4])


    print()
    print("inStock after a call to setInStock:")
    for row in range(len(inStock)):
        for column in range(len(inStock[row])):
            if column == 0:
                print(inStock[row][column], end = "\t")
            elif column == 3:
                inStock[row][column] = (inStock[row][column-1]*2) - delta[row]
                print(inStock[row][column], end = "\n")
            else:
                inStock[row][column] = (inStock[row][column-1]*2) - delta[row]
                print(inStock[row][column], end = "\t")



def main():
    #putting it all together
    setZero()
    print("Alpha after initialization:")
    printArray(alpha)
    inputArray()
    print("Alpha after reading 20 numbers:")
    printArray(alpha)
    print("Beta after a call to doubleArray:")
    doubleArray()
    printArray(beta)
    print("inStock after a call to copyGamma:")
    copyGamma()
    print("inStock after a call to copyAlphaBeta:")
    copyAlphaBeta()
    setInStock()



#Run the program
main()
