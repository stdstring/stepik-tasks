import typing
import unittest


class InputData(typing.NamedTuple):

    sequence1: typing.List[int]
    sequence2: typing.List[int]


def read_input_data(filename: str) -> InputData:
    with open(filename, 'r') as source:
        source.readline()
        sequence1 = list(map(int, source.readline().split()))
        source.readline()
        sequence2 = list(map(int, source.readline().split()))
        return InputData(sequence1, sequence2)


def calc_max_common_subsequence(input_data: InputData) -> int:
    dest = [[]]
    for _ in range(len(input_data.sequence2) + 1):
        dest[-1].append(0)
    for index1 in range(1, len(input_data.sequence1) + 1):
        dest.append([0])
        for index2 in range(1, len(input_data.sequence2) + 1):
            dest[-1].append(max(dest[index1 - 1][index2], dest[index1][index2 - 1]))
            if input_data.sequence1[index1 - 1] == input_data.sequence2[index2 - 1]:
                dest[index1][index2] = max(dest[index1][index2], dest[index1 - 1][index2 - 1] + 1)
    return dest[-1][-1]


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        input_data = InputData([3, 2, 4, 2, 1, 7, 6], [4, 2, 5, 3, 1, 6, 5, 2, 3])
        self.assertEqual(4, calc_max_common_subsequence(input_data))

    def test_task1(self):
        input_data = read_input_data("./seq.in")
        self.assertEqual(6, calc_max_common_subsequence(input_data))

    def test_task2(self):
        input_data = read_input_data("./seq2.in")
        self.assertEqual(79, calc_max_common_subsequence(input_data))


if __name__ == "__main__":
    unittest.main()