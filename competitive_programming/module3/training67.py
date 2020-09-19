import typing
import unittest


def read_sequence(filename: str) -> typing.List[int]:
    with open(filename, 'r') as source:
        source.readline()
        return list(map(int, source.readline().split()))


class Result(typing.NamedTuple):

    length: int
    count: int


def calc_max_increasing_subsequence(sequence: typing.List[int]) -> Result:
    subsequences_length = []
    subsequences_count = []
    for number in sequence:
        length = 1
        count = 1
        for index in range(len(subsequences_length) - 1, -1, -1):
            if sequence[index] < number:
                if length < (subsequences_length[index] + 1):
                    length = subsequences_length[index] + 1
                    count = subsequences_count[index]
                elif length == (subsequences_length[index] + 1):
                    count += subsequences_count[index]
        subsequences_length.append(length)
        subsequences_count.append(count)
    max_length = max(subsequences_length)
    count = 0
    for index in range(len(subsequences_length)):
        if subsequences_length[index] == max_length:
            count += subsequences_count[index]
    return Result(max_length, count)


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        sequence = [7, 1, 3, 2, 4]
        self.assertEqual(Result(3, 2), calc_max_increasing_subsequence(sequence))

    def test_task(self):
        sequence = read_sequence("./lis.in")
        self.assertEqual(Result(79, 2724495360), calc_max_increasing_subsequence(sequence))


if __name__ == "__main__":
    unittest.main()