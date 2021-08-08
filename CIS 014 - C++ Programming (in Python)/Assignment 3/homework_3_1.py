def separateLetters(inp: str) -> str:
    sortd = list(inp)
    for i in range(len(sortd)):
        j = i + 1
        jBefore = i

        for j in range(len(sortd)):
            if sortd[j] > sortd[jBefore]:
                jBefore = j

        if jBefore != i:
            sortd[i], sortd[jBefore] = sortd[jBefore], sortd[i]

    return ''.join(sortd)


def main():
    user = input('Input: ')
    print(f'Output: {separateLetters(user)}')


main()
