import typing
import unittest


class Thing(typing.NamedTuple):

    number: int
    weight: int
    cost: int


class InputData(typing.NamedTuple):

    backpack_weight: int
    things: typing.List[Thing]


def read_input_data(filename: str) -> InputData:
    def create_thing(number: int, line: str) -> Thing:
        [weight, cost] = list(map(int, line.split()))
        return Thing(number, weight, cost)
    with open(filename, 'r') as source:
        [n, backpack_weight] = list(map(int, source.readline().split()))
        things = list(map(lambda number: create_thing(number, source.readline()), range(1, n + 1)))
        return InputData(backpack_weight, things)


class Result(typing.NamedTuple):

    total_cost: int
    used_things: typing.List[int]


def calc_max_total_cost(input_data: InputData) -> Result:
    dest_total_cost = [[]]
    dest_things_usage = [[]]
    for _ in range(input_data.backpack_weight + 1):
        dest_total_cost[-1].append(0)
        dest_things_usage[-1].append(False)
    for thing in input_data.things:
        dest_total_cost.append([0])
        dest_things_usage.append([False])
        for weight in range(1, input_data.backpack_weight + 1):
            dest_total_cost[-1].append(dest_total_cost[thing.number - 1][weight])
            dest_things_usage[-1].append(False)
            if (weight - thing.weight) >= 0:
                if (dest_total_cost[thing.number - 1][weight - thing.weight] + thing.cost) > dest_total_cost[thing.number][weight]:
                    dest_total_cost[thing.number][weight] = max(dest_total_cost[thing.number][weight], dest_total_cost[thing.number - 1][weight - thing.weight] + thing.cost)
                    dest_things_usage[thing.number][weight] = True
    used_things = []
    things_weight = input_data.backpack_weight
    for thing in reversed(input_data.things):
        if dest_things_usage[thing.number][things_weight]:
            used_things.append(thing.number)
            things_weight -= thing.weight
    return Result(dest_total_cost[-1][input_data.backpack_weight], sorted(used_things))


class TestTaskImplementation(unittest.TestCase):

    def test_example1(self):
        input_data = InputData(12, [Thing(1, 2, 10), Thing(2, 5, 20), Thing(3, 10, 30)])
        self.assertEqual(Result(40, [1, 3]), calc_max_total_cost(input_data))

    def test_example2(self):
        input_data = InputData(12, [Thing(1, 2, 10), Thing(2, 5, 20), Thing(3, 8, 30)])
        self.assertEqual(Result(40, [1, 3]), calc_max_total_cost(input_data))

    def test_task(self):
        input_data = read_input_data("./rucksack.in")
        self.assertEqual(Result(58638, [1, 7, 14, 19, 42, 57, 60, 83, 89, 91]), calc_max_total_cost(input_data))


if __name__ == "__main__":
    unittest.main()