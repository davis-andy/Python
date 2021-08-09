def rightShiftElements(arr: list, N: int, M: int):
    x = N
    i = N - 1

    while M > N:
        M = M - N

    while i >= 0:
        if i >= M:
            arr[i] = arr[i - M]
        else:
            arr[i] = x
            x -= 1

        i -= 1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    size = len(arr)
    rightShiftElements(arr, size, 1)
    print('[', end='')
    for i in range(size):
        print(arr[i], end='')
        if i == size-1:
            print('', end='')
        else:
            print(',', end=' ')
    print(']')


main()
