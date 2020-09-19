import math
import typing
import unittest


def read_roads(filename: str) -> typing.List[typing.List[int]]:
    with open(filename, 'r') as source:
        n = int(source.readline())
        return list(map(lambda _: list(map(int, source.readline().split())), range(n)))


class Result(typing.NamedTuple):

    min_path_length: int
    min_path: typing.List[int]


def calc_min_path(roads: typing.List[typing.List[int]]) -> Result:
    cities_count = len(roads)
    city_mask_size = 1 << cities_count
    path_data = [[math.inf for _ in range(cities_count)] for _ in range(city_mask_size)]
    path_data[0][0] = 0
    city_data = [[None for _ in range(cities_count)] for _ in range(city_mask_size)]
    for mask in range(city_mask_size):
        for from_city in range(cities_count):
            if path_data[mask][from_city] == math.inf:
                continue
            for to_city in range(cities_count):
                if (mask & (1 << to_city)) == 0:
                    to_city_mask = mask | (1 << to_city)
                    to_city_path = path_data[mask][from_city] + roads[from_city][to_city]
                    if to_city_path <= path_data[to_city_mask][to_city]:
                        city_data[to_city_mask][to_city] = from_city
                        path_data[to_city_mask][to_city] = to_city_path
    path = []
    current_city = 0
    current_mask = city_mask_size - 1
    while current_mask > 0:
        from_city = city_data[current_mask][current_city]
        current_mask &= ~(1 << current_city)
        current_city = from_city
        path.append(current_city)
    return Result(path_data[city_mask_size - 1][0], list(reversed(path)))


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        roads = [[0, 1, 4, 6], [1, 0, 5, 2], [4, 5, 0, 3], [6, 2, 3, 0]]
        self.assertEqual(Result(10, [0, 1, 3, 2]), calc_min_path(roads))

    def test_task(self):
        roads = read_roads("./salesman2.in")
        self.assertEqual(Result(111, [0, 3, 10, 8, 6, 13, 14, 15, 2, 7, 1, 4, 9, 12, 11, 5]), calc_min_path(roads))


if __name__ == "__main__":
    unittest.main()