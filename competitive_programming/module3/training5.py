import math
import typing
import unittest


class InputData(typing.NamedTuple):

    total_sum: int
    coins: typing.List[int]


def read_input_data(filename: str) -> InputData:
    with open(filename, 'r') as source:
        [_, total_sum] = list(map(int, source.readline().split()))
        coins = list(map(int, source.readline().split()))
        return InputData(total_sum, coins)


def calc_min_coins_count(input_data: InputData) -> int:
    dest = [0]
    for current in range(1, input_data.total_sum + 1):
        dest.append(math.inf)
        for coin in input_data.coins:
            if (current - coin) >= 0:
                dest[-1] = min(dest[-1], dest[current - coin] + 1)
    return dest[-1]


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        input_data = InputData(39, [1, 2, 5, 10])
        self.assertEqual(6, calc_min_coins_count(input_data))

    def test_task(self):
        input_data = read_input_data("./change.in")
        self.assertEqual(235, calc_min_coins_count(input_data))


if __name__ == "__main__":
    unittest.main()