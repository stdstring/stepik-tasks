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


def calc_max_processed_requests(requests: typing.List[Request]) -> int:
    requests = sorted(requests, key=lambda request: request.right)
    processed_requests = 1
    last = requests[0]
    for index in range(1, len(requests)):
        current = requests[index]
        if last.right <= current.left:
            processed_requests += 1
            last = current
    return processed_requests


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        requests = [Request(1, 5), Request(3, 6), Request(5, 7)]
        self.assertEqual(2, calc_max_processed_requests(requests))

    def test_task1(self):
        requests = read_request_list("./request.in")
        self.assertEqual(4, calc_max_processed_requests(requests))

    def test_task2(self):
        requests = read_request_list("./request2.in")
        self.assertEqual(372, calc_max_processed_requests(requests))


if __name__ == "__main__":
    unittest.main()