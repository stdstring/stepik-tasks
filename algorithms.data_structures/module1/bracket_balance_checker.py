import typing


class Result(typing.NamedTuple):
    success: bool
    index: int


def process(source: str) -> Result:
    bracket_pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for index, ch in enumerate(source, start=1):
        if (ch in ["(", "[", "{"]):
            stack.append((ch, index))
        if (ch in [")", "]", "}"]):
            if len(stack) == 0:
                return Result(False, index)
            expected_bracket = bracket_pairs[ch]
            actual_bracket = stack.pop()[0]
            if expected_bracket != actual_bracket:
                return Result(False, index)
    return Result(True, 0) if len(stack) == 0 else Result(False, stack.pop()[1])


if __name__ == "__main__":
    result = process(input())
    if result.success:
        print("Success")
    else:
        print(result.index)
