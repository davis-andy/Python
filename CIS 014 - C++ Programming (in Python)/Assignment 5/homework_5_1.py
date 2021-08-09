def compareVersions(ver1: str, ver2: str) -> int:
    delim = '.'
    ver1List = []
    ver2List = []

    if ver1[0] == delim:
        ver1List.append('0')
    for char in ver1:
        ver1List.append(char)

    if ver2[0] == delim:
        ver2List.append('0')
    for char in ver2:
        ver2List.append(char)

    counter1 = 0
    counter2 = 0

    for i in ver1List:
        if i == delim:
            counter1 += 1
    for j in ver2List:
        if j == delim:
            counter2 += 1

    if counter1 > counter2:
        arraySize = counter1 + 1
    else:
        arraySize = counter2 + 1

    ver1num = []
    ver2num = []

    for i in range(arraySize):
        ver1num.append(0)
        ver2num.append(0)

    test1 = 0
    test2 = 0

    for step1 in ver1List:
        if step1 == delim:
            test1 += 1
        else:
            ver1num[test1] = ver1num[test1] * 10 + (int(step1))

    for step2 in ver2List:
        if step2 == delim:
            test2 += 1
        else:
            ver2num[test2] = ver2num[test2] * 10 + (int(step2))

    step = 0
    while step < arraySize:
        if ver1num[step] < ver2num[step]:
            return -1

        if ver1num[step] > ver2num[step]:
            return 1

        step += 1

    return 0


def main():
    print(compareVersions("0.1", "0.2"))  # -1
    print(compareVersions("0.1.1", "0.13.2"))  # -1
    print(compareVersions("1.0", "1.0"))  # 0
    print(compareVersions("6", "6"))  # 0
    print(compareVersions("0", "0"))  # 0
    print(compareVersions("1.1.0", "1.1.1"))  # -1
    print(compareVersions("1.1.1", "1.1.2"))  # -1
    print(compareVersions("1.1.2", "1.2.0"))  # -1
    print(compareVersions("1.2.0", "1.2.1"))  # -1
    print(compareVersions("1.2.1", "1.3.1"))  # -1
    print(compareVersions("1.3.1", "8.8.8"))  # -1
    print(compareVersions("1", "1.1"))  # -1
    print(compareVersions("1.1", "1.1.0"))  # 0
    print(compareVersions("256", "300.2.1"))  # -1
    print(compareVersions("0.1", "1"))  # -1
    print(compareVersions("3", "3.1.1"))  # -1
    print(compareVersions("3.1.1", "4"))  # -1
    print(compareVersions(".0.4", ".1"))  # -1
    print(compareVersions(".2", ".1.1"))  # 1
    print(compareVersions("2.3.2.2.3.1.1.5.3.5.6.2", "1.1.1.1.1.1.1"))  # 1


main()
