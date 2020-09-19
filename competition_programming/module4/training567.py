import typing
import unittest
from functools import lru_cache


@lru_cache
def generate_next_masks(row: int, m: int, mask: int) -> typing.List[int]:
    if row >= m:
        return [0]
    if (mask & 1) > 0:
        return generate_next_masks(row + 1, m, mask >> 1)
    else:
        row_mask = 1 << row
        next_masks = [next_mask | row_mask for next_mask in generate_next_masks(row + 1, m , mask >> 1)]
        if ((row + 1) < m) and (mask & 3 == 0):
            next_masks += [next_mask for next_mask in generate_next_masks(row + 2, m , mask >> 2)]
        return next_masks


def calc_dominos_count(n: int, m: int, k: int) -> int:
    n, m = (n, m) if n >= m else (m, n)
    mask_size = 1 << m
    dest = [[0 for _ in range(mask_size)] for _ in range (n + 1)]
    dest[0][0] = 1
    for column in range(n):
        for mask in range(mask_size):
            for next_mask in generate_next_masks(0, m, mask):
                dest[column + 1][next_mask] = (dest[column + 1][next_mask] + dest[column][mask]) % k
    return dest[-1][0]


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3, calc_dominos_count(3, 2, 10))

    def test_task1(self):
        self.assertEqual(1183, calc_dominos_count(5, 6, 1000000000))

    def test_task2(self):
        self.assertEqual(938355277, calc_dominos_count(5000, 6, 1000000000))

    def test_task3(self):
        self.assertEqual(79170816, calc_dominos_count(16, 16, 1000000000))


if __name__ == "__main__":
    unittest.main()
