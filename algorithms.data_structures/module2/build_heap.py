import typing


class ExchangeData(typing.NamedTuple):
    from_index: int
    to_index: int


def parent(current: int) -> int:
    return (current - 1) // 2


def left_child(current: int) -> int:
    return 2 * current + 1


def right_child(current: int) -> int:
    return 2 * current + 2


def sift_down(source: typing.List[int], index: int, exchanges: typing.List[ExchangeData]) -> None:
    max_index = index
    left = left_child(index)
    if (left < len(source)) and (source[left] < source[max_index]):
        max_index = left
    right = right_child(index)
    if (right < len(source)) and (source[right] < source[max_index]):
        max_index = right
    if index != max_index:
        value = source[index]
        source[index] = source[max_index]
        source[max_index] = value
        exchanges.append(ExchangeData(index, max_index))
        sift_down(source, max_index, exchanges)


def build_heap(source: typing.List[int]) -> typing.List[ExchangeData]:
    exchanges = []
    for index in range(len(source) // 2 - 1, -1, -1):
        sift_down(source, index, exchanges)
    return exchanges


if __name__ == "__main__":
    n = int(input())
    source = list(map(int, input().split()))
    exchanges = build_heap(source)
    print(len(exchanges))
    for exchange_data in exchanges:
        print(f"{exchange_data.from_index} {exchange_data.to_index}")