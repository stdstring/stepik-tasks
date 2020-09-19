import typing
import unittest


def read_numbers(filename: str) -> typing.List[int]:
    with open(filename, 'r') as source:
        source.readline()
        return list(map(int, source.readline().split()))


def calc_ones(numbers: typing.List[int]) -> typing.List[int]:
    dest = []
    for number in numbers:
        count = 0
        while number > 0:
            count += (number & 1)
            number >>= 1
        dest.append(count)
    return dest


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual([2, 3, 0], calc_ones([5, 13, 0]))

    def test_task(self):
        self.assertEqual([8, 15, 16, 17, 15, 16, 17, 15], calc_ones(read_numbers("./ones.in")))


if __name__ == "__main__":
    unittest.main()