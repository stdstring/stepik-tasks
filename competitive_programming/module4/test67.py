import typing
import unittest


class InputData(typing.NamedTuple):

    people_count: int
    friends_pairs: typing.List[typing.Tuple[int, int]]


def read_friends(filename: str) -> InputData:
    with open(filename, 'r') as source:
        [people_count, friends_pairs_count] = list(map(int, source.readline().split()))
        friends_pairs = list(map(lambda _: list(map(int, source.readline().split())), range(friends_pairs_count)))
        return InputData(people_count, friends_pairs)


def calc_max_company_size(input_data: InputData) -> int:
    people = [1 << man for man in range(input_data.people_count)]
    for [man1, man2] in input_data.friends_pairs:
        people[man1 - 1] |= (1 << (man2 - 1))
        people[man2 - 1] |= (1 << (man1 - 1))
    mask_size = 1 << input_data.people_count
    companies = [0 for _ in range(mask_size)]
    for mask in range(mask_size):
        for man in range(input_data.people_count):
            if ((mask & (1 << man)) > 0) and ((mask & people[man]) == mask):
                companies[mask] = companies[mask ^ (1 << man)] + 1
                break
    return max(companies)


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        data = InputData(4, [[1, 2], [2, 3], [3, 1], [2, 4]])
        self.assertEqual(3, calc_max_company_size(data))

    def test_task1(self):
        data = read_friends("./friends.in")
        self.assertEqual(3, calc_max_company_size(data))

    def test_task2(self):
        data = read_friends("./friends2.in")
        self.assertEqual(7, calc_max_company_size(data))


if __name__ == "__main__":
    unittest.main()