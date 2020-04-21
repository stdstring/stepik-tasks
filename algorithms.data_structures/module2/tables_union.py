import typing


class TableData(typing.NamedTuple):
    number: int
    rows_count: int


def get_head(tables: typing.List[TableData], table_number: int) -> TableData:
    table = tables[table_number - 1]
    if table.number == table_number:
        return table
    head = get_head(tables, table.number)
    tables[table_number - 1] = TableData(head.number, table.rows_count)
    return head


if __name__ == "__main__":
    [n, m] = list(map(int, input().split()))
    tables_rows_count = map(int, input().split())
    tables = list(map(lambda value: TableData(value[0], value[1]), enumerate(tables_rows_count, start=1)))
    max_rows_count = max(tables, key=lambda table: table.rows_count).rows_count
    max_rows_count_dest = []
    for _ in range(m):
        [destination, source] = list(map(int, input().split()))
        destination = get_head(tables, destination)
        source = get_head(tables, source)
        result_rows = destination.rows_count
        if source.number != destination.number:
            result_rows += source.rows_count
            tables[source.number - 1] = TableData(source.number, result_rows)
            tables[destination.number - 1] = TableData(source.number, 0)
        if max_rows_count < result_rows:
            max_rows_count = result_rows
        max_rows_count_dest.append(max_rows_count)
    for max_rows_count_value in max_rows_count_dest:
        print(max_rows_count_value)