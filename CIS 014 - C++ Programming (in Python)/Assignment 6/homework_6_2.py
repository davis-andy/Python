def plusPlusN(v: list) -> list:
    size1 = len(v) - 1
    size2 = len(v) - 1
    v[-1] += 1

    while size1 >= 0:
        if v[size1] == 10:
            if size1 - 1 != -1:
                v[size1 - 1] += 1
                v[size1] = 0
        size1 -= 1

    if v[0] == 10:
        v.append(v[-1])
        while size2 >= 0:
            v[size2] = v[size2 - 1]
            size2 -= 1
        v[1] = 0
        v[0] = 1

    return v


def main():
    v = [9, 9]
    retVal = plusPlusN(v)  # retVal = [1, 0, 0]
    print(retVal)


main()
