import typing
import unittest


def read_icecreams(filename: str) -> typing.List[str]:
    with open(filename, 'r') as source:
        n = int(source.readline())
        return list(map(lambda _: source.readline(), range(n)))


def calc_min_producer_count(icecreams: typing.List[str]) -> int:
    known_icecreams = set()
    current_producer = 1
    for icecream in icecreams:
        if icecream in known_icecreams:
            known_icecreams = set([icecream])
            current_producer += 1
        else:
            known_icecreams.add(icecream)
    return current_producer


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        icecreams = ["vanilla20", "pistachio", "strawberry", "blackberry", "vanilla20", "pistachio", "pistachio", "vanilla20"]
        self.assertEqual(3, calc_min_producer_count(icecreams))

    def test_task1(self):
        icecreams = read_icecreams("./ice.in")
        self.assertEqual(6, calc_min_producer_count(icecreams))

    def test_task2(self):
        icecreams = read_icecreams("./ice2.in")
        self.assertEqual(88, calc_min_producer_count(icecreams))


if __name__ == "__main__":
    unittest.main()