import unittest


def calc_dominos_count(n: int, m: int) -> int:
    storage = [1, 1]
    for _ in range(2, n + 1):
        storage.append((storage[-1] + storage[-2]) % m)
    return storage[-1]


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1, calc_dominos_count(4, 4))

    def test_task1(self):
        self.assertEqual(37, calc_dominos_count(42, 100))

    def test_task2(self):
        self.assertEqual(707537501, calc_dominos_count(100000, 1000000000))


if __name__ == "__main__":
    unittest.main()