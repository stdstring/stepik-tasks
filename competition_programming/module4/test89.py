import math
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


def calc_min_news_subset_size(input_data: InputData) -> int:
    people = [1 << man for man in range(input_data.people_count)]
    for [man1, man2] in input_data.friends_pairs:
        people[man1 - 1] |= (1 << (man2 - 1))
        people[man2 - 1] |= (1 << (man1 - 1))
    mask_size = 1 << input_data.people_count
    news_subsets = [math.inf for _ in range(mask_size)]
    news_subsets[0] = 0
    processed_masks = [0]
    while len(processed_masks) > 0:
        mask = processed_masks.pop(0)
        for man in range(input_data.people_count):
            new_mask = mask | (1 << man) | people[man]
            old_value = news_subsets[new_mask]
            new_value = min(news_subsets[new_mask], news_subsets[mask] + (0 if (mask & people[man]) == people[man] else 1))
            if new_value < old_value:
                news_subsets[new_mask] = new_value
                processed_masks.append(new_mask)
    return news_subsets[mask_size - 1]


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        data = InputData(4, [[1, 2], [2, 3], [3, 4]])
        self.assertEqual(2, calc_min_news_subset_size(data))

    def test_task1(self):
        data = read_friends("./new.in")
        self.assertEqual(3, calc_min_news_subset_size(data))

    def test_task2(self):
        data = read_friends("./new2.in")
        self.assertEqual(6, calc_min_news_subset_size(data))


if __name__ == "__main__":
    unittest.main()