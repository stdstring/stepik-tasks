import unittest


def calc_binominal_coeff(n: int, k: int) -> int:
    current_row = [1]
    for number_n in range(1, n + 1):
        next_row = [1]
        for number_k in range(1, number_n):
            next_row.append(current_row[number_k - 1] + current_row[number_k])
        next_row.append(1)
        current_row = next_row
    return current_row[k]


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3, calc_binominal_coeff(3, 2))

    def test_task(self):
        self.assertEqual(47129212243960, calc_binominal_coeff(50, 20))


if __name__ == "__main__":
    unittest.main()