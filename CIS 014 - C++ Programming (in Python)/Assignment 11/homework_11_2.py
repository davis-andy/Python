def getMaxPond(arr: list, size: int) -> int:
    begin = 0
    end = size - 1
    firstNum = arr[0]
    lastNum = arr[-1]

    # result is smallest number from either end of the array times the array size (initially)
    result = min(firstNum, lastNum) * (size - 1)

    # check to see if we can get bigger holes from digging
    while begin < end:
        # start from beginning if the first number is smaller
        if firstNum <= lastNum:
            begin += 1
            # if next number is bigger, then dig
            if arr[begin] > firstNum:
                firstNum = arr[begin]  # dug a hole
                tmp = min(firstNum, lastNum) * (end - begin)
                result = max(result, tmp)
        else:
            end -= 1
            if arr[end] > lastNum:
                lastNum = arr[end]
                tmp = min(firstNum, lastNum) * (end - begin)
                result = max(result, tmp)

    return result


def main():
    # test cases
    arr1 = [22, 31, 1, 23]
    size1 = len(arr1)

    arr2 = [1]
    size2 = len(arr2)

    arr3 = [1, 3, 5]
    size3 = len(arr3)

    arr4 = [3, 2, 1]
    size4 = len(arr4)

    arr5 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    size5 = len(arr5)

    arr6 = [1, 99, 1]
    size6 = len(arr6)

    # print results
    print(getMaxPond(arr1, size1))  # 66
    print(getMaxPond(arr2, size2))  # 0
    print(getMaxPond(arr3, size3))  # 3
    print(getMaxPond(arr4, size4))  # 2
    print(getMaxPond(arr5, size5))  # 8
    print(getMaxPond(arr6, size6))  # 2


# run program
main()