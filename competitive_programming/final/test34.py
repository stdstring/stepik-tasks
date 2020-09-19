import typing
import unittest


class InputData(typing.NamedTuple):

    shops: typing.List[int]
    storages: typing.List[int]


def read_input_data(filename: str) -> InputData:
    with open(filename, 'r') as source:
        _ = int(source.readline())
        shops = list(map(int, source.readline().split()))
        storages = list(map(int, source.readline().split()))
        return InputData(shops, storages)


def calc_best_shop_storage_links(input_data: InputData) -> int:
    shops = sorted(input_data.shops)
    storages = sorted(input_data.storages)
    return sum(map(lambda index: abs(shops[index] - storages[index]), range(len(shops))))


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        data = InputData([3, 5], [6, 2])
        self.assertEqual(2, calc_best_shop_storage_links(data))

    def test_task1(self):
        data = read_input_data("./shops.in")
        self.assertEqual(1129, calc_best_shop_storage_links(data))

    def test_task2(self):
        data = read_input_data("./shops2.in")
        self.assertEqual(95580888489, calc_best_shop_storage_links(data))


if __name__ == "__main__":
    unittest.main()