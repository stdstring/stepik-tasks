import typing
import unittest


class Request(typing.NamedTuple):

    left: int
    right: int


def read_request_list(filename: str) -> typing.List[Request]:
    def create_request(line: str) -> Request:
        [left, right] = list(map(int, line.split()))
        return Request(left, right)
    with open(filename, 'r') as source:
        n = int(source.readline())
        return list(map(lambda _: create_request(source.readline()), range(n)))


def calc_min_used_classrooms(requests: typing.List[Request]) -> int:
    borders = []
    for request in requests:
        borders.append((request.left, 1))
        borders.append((request.right, -1))
    borders = sorted(borders)
    max_used_classrooms = 0
    used_classrooms = 0
    for (_, delta) in borders:
        used_classrooms += delta
        if used_classrooms > max_used_classrooms:
            max_used_classrooms = used_classrooms
    return max_used_classrooms


class TestTaskImplementation(unittest.TestCase):

    def test_example1(self):
        requests = [Request(1, 5), Request(3, 6), Request(5, 7)]
        self.assertEqual(2, calc_min_used_classrooms(requests))

    def test_example2(self):
        requests = [Request(2, 6), Request(0, 1), Request(1, 2), Request(2, 5), Request(0, 1), Request(0, 2), Request(2, 4), Request(2, 7), Request(1, 2), Request(2, 3)]
        self.assertEqual(5, calc_min_used_classrooms(requests))

    def test_example3(self):
        requests = [Request(2, 3), Request(1, 5), Request(6, 7), Request(4, 8)]
        self.assertEqual(2, calc_min_used_classrooms(requests))

    def test_task(self):
        requests = read_request_list("./request2.in")
        self.assertEqual(50038, calc_min_used_classrooms(requests))


if __name__ == "__main__":
    unittest.main()