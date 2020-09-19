import typing
import unittest


def read_gold_bars(filename: str) -> typing.List[int]:
    with open(filename, 'r') as source:
        _ = int(source.readline())
        return list(map(int, source.readline().split()))


def calc_max_partition_diff(gold_bars: typing.List[int]) -> int:
    gold_bars = sorted(gold_bars)
    return sum(gold_bars[len(gold_bars) // 2:]) - sum(gold_bars[:len(gold_bars) // 2])


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4, calc_max_partition_diff([1, 2, 3, 4]))

    def test_task(self):
        data = read_gold_bars("./gold4.in")
        self.assertEqual(124759532, calc_max_partition_diff(data))


if __name__ == "__main__":
    unittest.main()