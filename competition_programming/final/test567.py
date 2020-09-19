import typing
import unittest


def read_gold_bars(filename: str) -> typing.List[int]:
    with open(filename, 'r') as source:
        _ = int(source.readline())
        return list(map(int, source.readline().split()))


def calc_min_partition_diff(gold_bars: typing.List[int]) -> int:
    total_weight = sum(gold_bars)
    knapsack_weight = total_weight // 2
    current = set()
    for gold_bar_index in range(len(gold_bars)):
        next = set([gold_bars[gold_bar_index]])
        for weight in current:
            next.add(weight)
            if (weight + gold_bars[gold_bar_index]) <= knapsack_weight:
                next.add(weight + gold_bars[gold_bar_index])
        current = next
    for weight in range(knapsack_weight, -1, -1):
        if weight in current:
            return total_weight - 2 * weight


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1, calc_min_partition_diff([1, 2, 3, 4, 5]))

    def test_task1(self):
        data = read_gold_bars("./gold.in")
        self.assertEqual(20, calc_min_partition_diff(data))

    def test_task2(self):
        data = read_gold_bars("./gold2.in")
        self.assertEqual(253, calc_min_partition_diff(data))

    def test_task3(self):
        data = read_gold_bars("./gold3.in")
        self.assertEqual(1906, calc_min_partition_diff(data))


if __name__ == "__main__":
    unittest.main()