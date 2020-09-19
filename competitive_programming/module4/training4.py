import typing
import unittest


def generate_subsets(n: int) -> typing.List[typing.List[int]]:
    dest = []
    for mask in range(1 << n):
        current = []
        for index in range(n):
            if (mask & (1 << index)) > 0:
                current.append(index + 1)
        dest.append(current)
    return dest


def create_representation(subsets: typing.List[typing.List[int]]) -> typing.List[str]:
    return sorted(map(lambda subset: "{{{}}}".format(",".join(map(str, subset))) ,subsets))


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual("{2,3}", create_representation(generate_subsets(3))[5 - 1])

    def test_task(self):
        self.assertEqual("{2,5,8,9}", create_representation(generate_subsets(9))[365 - 1])


if __name__ == "__main__":
    unittest.main()