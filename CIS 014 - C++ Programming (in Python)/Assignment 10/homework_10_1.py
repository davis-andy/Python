class CIS14:
    def getMaxPoints(self, maze: list) -> int:
        i = len(maze) - 2  # start at the second from the bottom row

        # check if the maze is empty and return 0
        if len(maze) == 0:
            return 0

        while i >= 0:
            # empty input returns 0
            if len(maze[i]) == 0:
                return 0

            for currentPos in range(len(maze[i])):
                # check which item is bigger in the row below current row
                if maze[i + 1][currentPos] > maze[i + 1][currentPos + 1]:
                    # if the left item is bigger, add to score
                    maze[i][currentPos] += maze[i + 1][currentPos]
                else:
                    # if the right item is bigger, add to score
                    maze[i][currentPos] += maze[i + 1][currentPos + 1]

            # decrement for the loop
            i -= 1

        # working from the bottom results in our score being the first item in the maze
        return maze[0][0]


def main():
    # test cases
    maze = [[2], [4, 1], [5, 3, 8], [1, 6, 7, 3]]
    mazeB = [[0], [4, 1], [5, 3, 8], [1, 6, 7, 3]]
    mazeC = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]
    mazeD = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    mazeE = [[1], [1, 22305], [1, 29394, 1], [1, 1, 1234, 1], [1, 1, 3, 1, 10]]
    mazeF = [[], [], [], []]
    mazeG = []

    # create class
    cis = CIS14()

    # print results
    print(cis.getMaxPoints(maze))  # 18
    print(cis.getMaxPoints(mazeB))  # 16
    print(cis.getMaxPoints(mazeC))  # 4
    print(cis.getMaxPoints(mazeD))  # 23
    print(cis.getMaxPoints(mazeE))  # 52937
    print(cis.getMaxPoints(mazeF))  # 0
    print(cis.getMaxPoints(mazeG))  # 0


# run program
main()
