def findHalfDuplicate(s: str) -> str:
    if len(s) <= 2 or len(s) % 2 != 0:
        return 'Invalid input'

    occur = len(s) / 2
    chars = {}
    result = ''

    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for k, v in chars.items():
        if v == occur:
            result = k

    return result


print(findHalfDuplicate("1a2a3a4a"))
print(findHalfDuplicate("a2a3a1"))
print(findHalfDuplicate("2aa3"))
print(findHalfDuplicate("2"))
print(findHalfDuplicate("2a"))
