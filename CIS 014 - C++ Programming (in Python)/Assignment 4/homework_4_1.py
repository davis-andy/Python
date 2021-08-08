def reverseString(inp: str) -> str:
    inpList = list(inp)
    i = len(inpList)-1
    result = []
    while i >= 0:
        result.append(inpList[i])
        i -= 1

    return ''.join(result)


def getShortestLength(n: int) -> int:
    strNum = str(n)
    backwards = reverseString(strNum)
    result = 0
    addOn = ''
    counter = 0

    if n < 0:
        return result

    elif strNum == backwards:
        result = len(strNum)

    else:
        for i in range(len(backwards)):
            addOn += backwards[i]
            tCheck = reverseString(addOn)
            if addOn == tCheck:
                counter = i + 1

        addOnList = list(addOn)[counter:]
        addOn = ''.join(addOnList)
        palindromeStr = strNum + addOn
        palindromeLength = len(palindromeStr)
        result = palindromeLength

    return result


def main():
    print(getShortestLength(121))
    print(getShortestLength(12393))
    print(getShortestLength(123))
    print(getShortestLength(-234))
    print(getShortestLength(4))
    print(getShortestLength(12434434))


main()
