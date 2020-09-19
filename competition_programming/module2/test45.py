import typing
import unittest


class Thing(typing.NamedTuple):

    weight: int
    cost: int


class InputData(typing.NamedTuple):

    backpack_weight: int
    things: typing.List[Thing]


def read_input_data(filename: str) -> InputData:
    def create_thing(line: str) -> Thing:
        [weight, cost] = list(map(int, line.split()))
        return Thing(weight, cost)
    with open(filename, 'r') as source:
        [n, backpack_weight] = list(map(int, source.readline().split()))
        things = list(map(lambda _: create_thing(source.readline()), range(n)))
        return InputData(backpack_weight, things)


def calc_backpack_max_cost(input_data: InputData) -> int:
    backpack_weight = input_data.backpack_weight
    total_cost = 0
    things = sorted(input_data.things, key=lambda thing : thing.cost // thing.weight, reverse=True)
    for thing in things:
        if thing.weight >= backpack_weight:
            return total_cost + (backpack_weight) * thing.cost // thing.weight
        total_cost += thing.cost
        backpack_weight -= thing.weight
    return total_cost


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        input_data = InputData(4, [Thing(2, 10), Thing(3, 12)])
        self.assertEqual(18, calc_backpack_max_cost(input_data))

    def test_task1(self):
        input_data = read_input_data("./cont.in")
        self.assertEqual(550, calc_backpack_max_cost(input_data))

    def test_task2(self):
        input_data = read_input_data("./cont2.in")
        self.assertEqual(7909205, calc_backpack_max_cost(input_data))


if __name__ == "__main__":
    unittest.main()