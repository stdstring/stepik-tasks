import typing
import unittest


class InputData(typing.NamedTuple):

    total_distance: int
    full_tank_distance: int
    gas_stations: typing.List[int]


def read_input_data(filename: str) -> InputData:
    with open(filename, 'r') as source:
        [_, total_distance, full_tank_distance] = list(map(int, source.readline().split()))
        gas_stations = list(map(int, source.readline().split()))
        return InputData(total_distance, full_tank_distance, gas_stations)


def calc_min_used_gas_stations(input_data: InputData) -> int:
    used_gas_stations = 0
    last_used_gas_station = 0
    for index in range(len(input_data.gas_stations)):
        current_gas_station = input_data.gas_stations[index]
        if (current_gas_station - last_used_gas_station) > input_data.full_tank_distance:
            last_used_gas_station = input_data.gas_stations[index - 1]
            used_gas_stations += 1
    if (input_data.total_distance - last_used_gas_station) > input_data.full_tank_distance:
        used_gas_stations += 1
    return used_gas_stations


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        input_data = InputData(10, 4, [3, 4, 6])
        self.assertEqual(2, calc_min_used_gas_stations(input_data))

    def test_task1(self):
        input_data = read_input_data("./petrol.in")
        self.assertEqual(4, calc_min_used_gas_stations(input_data))

    def test_task2(self):
        input_data = read_input_data("./petrol2.in")
        self.assertEqual(1021, calc_min_used_gas_stations(input_data))


if __name__ == "__main__":
    unittest.main()