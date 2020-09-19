import typing
import unittest


class Board(typing.NamedTuple):

    n: int
    m: int
    values: typing.List[typing.List[int]]


def read_board(filename: str) -> Board:
    with open(filename, 'r') as source:
        [n, m] = list(map(int, source.readline().split()))
        board = []
        for _ in range(n):
            board.append(list(map(int, source.readline().split())))
        return Board(n, m, board)


class Result(typing.NamedTuple):

    sum_value: int
    path: str


def find_best_path(board: Board) -> Result:
    d = []
    p = []
    # calc best sum
    for i in range (board.n):
        d.append([])
        p.append([])
        for j in range(board.m):
            d[-1].append(board.values[i][j])
            p[-1].append(-1)
            if (i > 0) and ((d[i - 1][j] + board.values[i][j]) > d[i][j]):
                d[i][j] = d[i - 1][j] + board.values[i][j]
                p[i][j] = 0
            if (j > 0) and ((d[i][j - 1] + board.values[i][j]) > d[i][j]):
                d[i][j] = d[i][j - 1] + board.values[i][j]
                p[i][j] = 1
    sum_value = d[-1][-1]
    # calc path
    path = ""
    i = board.n - 1
    j = board.m - 1
    while (i > 0) or (j > 0):
        if p[i][j] == 0:
            path = "D" + path
            i -= 1
        else:
            path = "R" + path
            j -= 1
    return Result(sum_value, path)


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        board = Board(3, 4, [[5, 3, 2, 2], [2, 1, 7, 3], [4, 3, 1, 2]])
        self.assertEqual(Result(22, 'RRDRD'), find_best_path(board))

    def test_task1(self):
        board = read_board("./bug.in")
        path = "DDDRDRRRRRRRRRRRRRRDRRRDRRRDRDRDDRRRDRDRRRRRRDRRRRRRDRRDRRRRDRDDDRRDRRDRRDDDRRDRDRDDDRDRRRDRDDDDRRDDRDRDRDDDDDRDDDDRRRDDDDRDDDRRRDRDRDRDRDDDRRRRDDRDDDDRDDDDRDDDRDRRRRRRDDRRRRDDDRDRRRRDRDRRDDRDDRDRRRDRRDRDRDDDDDDRRRDRRR"
        self.assertEqual(Result(16149, path), find_best_path(board))

    def test_task2(self):
        board = read_board("./bug2.in")
        self.assertEqual(Result(804, "RDDRRDRDDRRRD"), find_best_path(board))


if __name__ == "__main__":
    unittest.main()