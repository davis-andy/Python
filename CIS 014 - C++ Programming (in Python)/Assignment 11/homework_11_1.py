def getTotalWaterAmount(arr: list, size: int) -> int:
    length = size - 1
    elev = arr[0]
    elevIndex = 0
    totalWater = 0
    temp = 0

    # total all of the water from left to right
    # remember the tallest peak
    for i in range(length + 1):
        if arr[i] >= elev:
            elev = arr[i]
            elevIndex = i
            temp = 0
        else:
            totalWater += elev - arr[i]
            temp += elev - arr[i]

    # remove water that was counted twice
    # total all of the water from right to left
    if elevIndex < length:
        totalWater -= temp
        elev = arr[length]
        j = length

        while j >= elevIndex:
            if arr[j] >= elev:
                elev = arr[j]
            else:
                totalWater += elev - arr[j]
            j -= 1

    return totalWater


def main():
    # test cases
    arr1 = [10, 20, 30, 40, 42, 40, 30, 20, 40, 50, 55, 50, 40, 30, 20, 10, 3]
    size1 = len(arr1)

    arr2 = [5, 2, 1, 2, 1, 5]
    size2 = len(arr2)

    arr3 = [0, 1, 0]
    size3 = len(arr3)

    arr4 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 6, 22, 3, 2]
    size4 = len(arr4)

    arr5 = [0, 1, 2, 5, 4, 2, 6, 4, 3, 2, 1, 1, 1, 1, 1, 1, 8]
    size5 = len(arr5)

    arr6 = [5, 4, 1, 2]
    size6 = len(arr6)

    arr7 = [5, 2, 1, 3, 1, 5]
    size7 = len(arr7)

    arr8 = [5, 2, 1, 2, 1, 5, 4, 2]
    size8 = len(arr8)

    arr9 = [5, 2, 5, 2, 5, 5]
    size9 = len(arr9)

    arr10 = [5, 2, 5, 2, 5, 2, 5, 2, 5]
    size10 = len(arr10)

    # print results
    print(getTotalWaterAmount(arr1, size1))  # 38
    print(getTotalWaterAmount(arr2, size2))  # 14
    print(getTotalWaterAmount(arr3, size3))  # 0
    print(getTotalWaterAmount(arr4, size4))  # 6
    print(getTotalWaterAmount(arr5, size5))  # 43
    print(getTotalWaterAmount(arr6, size6))  # 1
    print(getTotalWaterAmount(arr7, size7))  # 13
    print(getTotalWaterAmount(arr8, size8))  # 14
    print(getTotalWaterAmount(arr9, size9))  # 6
    print(getTotalWaterAmount(arr10, size10))  # 12


# run program
main()
