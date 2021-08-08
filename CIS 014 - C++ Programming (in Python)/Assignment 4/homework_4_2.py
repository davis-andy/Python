def deduplicate(inp: str) -> str:
    i = 0
    j = 0

    if len(inp) == 1:
        return inp

    while i < len(inp)-1:
        while j < len(inp)-1:
            if j + 1 > len(inp) - 1:
                break
            elif inp[j] == inp[j+1]:
                inp = inp[:j] + inp[j + 2:]
            else:
                j += 1

        if i + 1 > len(inp) - 1:
            break
        elif inp[i] == inp[i + 1]:
            inp = inp[:i] + inp[i + 2:]
        else:
            i += 1

    if inp == '':
        inp = 'Empty'

    return inp


def main():
    print(deduplicate("AABB"))  # should output "Empty"
    print(deduplicate("A"))  # "A"
    print(deduplicate("ABBA"))  # should output "Empty"
    print(deduplicate("AAA"))  # "A"
    print(deduplicate("AKA"))  # "AKA" because there is no consecutive pair.


main()
