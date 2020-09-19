import typing
import unittest


def generate(n: int, m: int, lex_number: int) -> typing.List[int]:
    lex_number_rest = lex_number - 1
    sequence = []
    while len(sequence) < n:
        element = (lex_number_rest % m) + 1
        lex_number_rest = lex_number_rest // m
        sequence.insert(0, element)
    return sequence


class TestTaskImplementation(unittest.TestCase):

    def test_task(self):
        n = 6
        m = 5
        lex_number = 6659
        self.assertEqual([3, 1, 4, 2, 2, 4], generate(n, m, lex_number))


if __name__ == "__main__":
    unittest.main()