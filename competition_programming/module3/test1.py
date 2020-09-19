import typing
import unittest


class Query(typing.NamedTuple):

    from_row: int
    to_row: int
    from_column: int
    to_column: int


class InputData(typing.NamedTuple):

    row_count: int
    column_count: int
    matrix: typing.List[typing.List[int]]
    queries: typing.List[Query]


def read_input_data(filename: str) -> InputData:
    def read_query(line: str) -> Query:
        [from_row, to_row, from_column, to_column] = list(map(int, line.split()))
        return Query(from_row, to_row, from_column, to_column)
    with open(filename, 'r') as source:
        [row_count, column_count] = list(map(int, source.readline().split()))
        matrix = []
        for _ in range(row_count):
            row = list(map(int, source.readline().split()))
            matrix.append(row)
        query_count = int(source.readline())
        queries = list(map(lambda _: read_query(source.readline()), range(query_count)))
        return InputData(row_count, column_count, matrix, queries)


def process_queries(input_data: InputData) -> int:
    partial_sum_data = []
    for row in range(input_data.row_count):
        partial_sum_data.append([])
        for column in range(input_data.column_count):
            value = input_data.matrix[row][column]
            if row > 0:
                value += partial_sum_data[row - 1][column]
            if column > 0:
                value += partial_sum_data[row][column - 1]
            if (row > 0) and (column > 0):
                value -= partial_sum_data[row - 1][column - 1]
            partial_sum_data[-1].append(value)
    queries_result = 0
    for query in input_data.queries:
        rectangle_sum = partial_sum_data[query.to_row - 1][query.to_column - 1]
        if query.from_row > 1:
            rectangle_sum -= partial_sum_data[query.from_row - 2][query.to_column - 1]
        if query.from_column > 1:
            rectangle_sum -= partial_sum_data[query.to_row - 1][query.from_column - 2]
        if (query.from_row > 1) and (query.from_column > 1):
            rectangle_sum += partial_sum_data[query.from_row - 2][query.from_column - 2]
        queries_result += rectangle_sum
    return queries_result


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        matrix = [[1, 3, 7, -1, 7, 11], [2, 6, 5, 1, 1, 3], [-3, 0, 2, 0, 3, 8], [5, 1, 3, 1, 4, 7], [6, 1, -2, 2, 1, 0]]
        input_data = InputData(5, 6, matrix, [Query(2, 3, 2, 3), Query(1, 1, 5, 6), Query(3, 5, 3, 6)])
        self.assertEqual(60, process_queries(input_data))

    def test_task(self):
        input_data = read_input_data("./rectangle.in")
        self.assertEqual(329360892867, process_queries(input_data))


if __name__ == "__main__":
    unittest.main()
