import typing
import unittest


class InputData(typing.NamedTuple):

    target: int
    numbers: typing.List[int]


def read_input_data(filename: str) -> InputData:
    with open(filename, 'r') as source:
        [_, target] = list(map(int, source.readline().split()))
        numbers = list(map(int, source.readline().split()))
        return InputData(target, numbers)


def find_arith_expression(input_data: InputData) -> typing.Optional[str]:
    current_results = {input_data.numbers[0]: str(input_data.numbers[0])}
    for index in range(1, len(input_data.numbers)):
        next_results = {}
        number = input_data.numbers[index]
        for value in current_results:
            value_add = value + number
            if value_add not in next_results:
                next_results[value_add] = current_results[value] + "+" + str(number)
            value_sub = value - number
            if value_sub not in next_results:
                next_results[value_sub] = current_results[value] + "-" + str(number)
        current_results = next_results
    return current_results[input_data.target] if input_data.target in current_results else ""


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        data = InputData(0, [1, 2, 3])
        self.assertEqual("1+2-3", find_arith_expression(data))

    def test_task1(self):
        data = read_input_data("./arithm.in")
        self.assertEqual("21-27+34+20-29-24+38+38-22-24", find_arith_expression(data))

    def test_task2(self):
        data = read_input_data("./arithm2.in")
        expected = "91-67-84-50-69-74-78-58-62-64-55-95-81-77-61-91-95-92-77-86-91-54-52-53-92-82-71-66-68-95-97-76-71+88-69-62-67-99-85-94-53-61-72-83-73-64-91-61-53-68"
        self.assertEqual(expected, find_arith_expression(data))


if __name__ == "__main__":
    unittest.main()