import math
import typing
import unittest


class Result(typing.NamedTuple):

    length: int
    path: typing.List[int]


def find_best_path(n: int, a: typing.List[typing.List[int]]) -> Result:
    def find_best_path_impl(used_cities_mask: int, current_result: Result, best_result: Result) -> Result:
        for city in range(1, n):
            if (used_cities_mask & (1 << city)) > 0:
                continue
            if len(current_result.path) == (n - 1):
                updated_length = current_result.length + a[current_result.path[-1]][city] + a[city][0]
                return best_result if updated_length >= best_result.length else Result(updated_length, current_result.path + [city])
            else:
                updated_length = current_result.length + a[current_result.path[-1]][city]
                if updated_length >= best_result.length:
                    continue
                else:
                    best_result = find_best_path_impl(used_cities_mask | (1 << city), Result(updated_length, current_result.path + [city]), best_result)
        return best_result
    return find_best_path_impl(1, Result(0, [0]), Result(math.inf, []))


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        n = 4
        a = [[0, 1, 4, 6],
             [1, 0, 5, 2],
             [4, 5, 0, 3],
             [6, 2, 3, 0]]
        self.assertEqual(Result(10, [0, 1, 3, 2]), find_best_path(n, a))

    def test_task(self):
        n = 10
        a = [[0, 41, 67, 0, 78, 5, 91, 4, 18, 67],
             [41, 0, 34, 69, 58, 45, 95, 2, 95, 99],
             [67, 34, 0, 24, 62, 81, 42, 53, 47, 35],
             [0, 69, 24, 0, 64, 27, 27, 92, 26, 94],
             [78, 58, 62, 64, 0, 61, 36, 82, 71, 3],
             [5, 45, 81, 27, 61, 0, 91, 21, 38, 11],
             [91, 95, 42, 27, 36, 91, 0, 16, 69, 22],
             [4, 2, 53, 92, 82, 21, 16, 0, 12, 33],
             [18, 95, 47, 26, 71, 38, 69, 12, 0, 73],
             [67, 99, 35, 94, 3, 11, 22, 33, 73, 0]]
        self.assertEqual(Result(171, [0, 3, 8, 7, 1, 2, 6, 4, 9, 5]), find_best_path(n, a))


if __name__ == "__main__":
    unittest.main()
