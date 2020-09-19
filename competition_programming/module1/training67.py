import typing
import unittest


def generate(n: int, m: int) -> typing.List[str]:
    current_arrangements = list(map(lambda _: [], range(0, m + 1)))
    current_arrangements[0] = ["."]
    current_arrangements[1] = ["*"]
    for _ in range(1, n):
        next_arrangements = list(map(lambda _: [], range(0, m + 1)))
        for chip_count in range(0, m + 1):
            for row in current_arrangements[chip_count]:
                next_arrangements[chip_count].append("." + row)
                if (chip_count < m) and (row[0] != "*"):
                    next_arrangements[chip_count + 1].append("*" + row)
        current_arrangements = next_arrangements
    return current_arrangements[-1]


class TestTaskImplementation(unittest.TestCase):

    def test_task1(self):
        n = 7
        m = 3
        lex_number = 7
        self.assertEqual(".*.*.*.", generate(n, m)[lex_number - 1])

    def test_task2(self):
        n = 25
        m = 8
        lex_number = 24008
        self.assertEqual(".*.*.....*.*.*.*....*..*.", generate(n, m)[lex_number - 1])


if __name__ == "__main__":
    unittest.main()