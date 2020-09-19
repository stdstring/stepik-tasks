import typing
import unittest


def generate(n: int) -> typing.List[typing.List[int]]:
    terms = [[[1]]]
    for number in range(2, n + 1):
        current = []
        for term in range(1, number // 2 + 1):
            for combination in terms[number - term - 1]:
                if term <= combination[0]:
                    current.append([term] + combination)
        current.append([number])
        terms.append(current)
    return terms[-1]


class TestTaskImplementation(unittest.TestCase):

    def test_task1(self):
        n = 7
        lex_number = 10
        self.assertEqual([1, 3, 3], generate(n)[lex_number - 1])

    def test_task2(self):
        n = 35
        lex_number = 13672
        self.assertEqual([2, 3, 3, 4, 4, 6, 13], generate(n)[lex_number - 1])


if __name__ == "__main__":
    unittest.main()