def getLegoCombinations(lego_heights: list, target_height: int) -> int:
    # Create a matrix of possible outcomes based on number of bricks
    # ex: list = [target height] [possible times to build with brick sizes]
    result = [[0] * (target_height + 1)] * (len(lego_heights) + 1)

    for i in range(len(lego_heights) + 1):
        result[i][0] = 1  # only 1 way to get a height of 0 (no bricks)

    for x in range(1, len(lego_heights) + 1):
        for y in range(1, target_height + 1):
            if lego_heights[x - 1] <= y:  # if brick height is less than target height
                result[x][y] = result[x - 1][y] + result[x][y - lego_heights[x - 1]]  # include
            else:
                result[x][y] = result[x - 1][y]  # do not include

    if target_height == 0:
        return 0

    return result[len(lego_heights)][target_height]


def main():
    a = [1, 2, 5]
    b = [5]

    print(getLegoCombinations(a, 3))  # 2
    print(getLegoCombinations(a, 0))  # 0
    print(getLegoCombinations(a, 7))  # 6
    print(getLegoCombinations(b, 9))  # 0


main()
