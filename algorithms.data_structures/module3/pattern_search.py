import typing


p = 1000000007
x = 263
max_size = 500000


def calc_x_powers() -> typing.List[int]:
    x_powers = [1]
    for power in range(1, max_size):
        x_powers.append((x_powers[power - 1] * x) % p)
    return x_powers


x_powers = calc_x_powers()


def calc_hash(source: str, start: int) -> int:
    result = 0
    for index in range(len(source) - start):
        result += ord(source[start + index]) * x_powers[index]
        result = result % p
    return result


def compare_at_pos(text: str, pattern: str, start: int) -> bool:
    return pattern == text[start: start + len(pattern)]


if __name__ == "__main__":
    pattern = input()
    text = input()
    match_positions = []
    pattern_hash = calc_hash(pattern, 0)
    text_hash = calc_hash(text, len(text) - len(pattern))
    if (pattern_hash == text_hash) and compare_at_pos(text, pattern, len(text) - len(pattern)):
        match_positions.append(len(text) - len(pattern))
    for position in range(len(text) - len(pattern) - 1, -1, -1):
        text_hash = ((text_hash - ord(text[position + len(pattern)]) * x_powers[len(pattern) - 1]) * x + ord(text[position])) % p
        if (pattern_hash == text_hash) and compare_at_pos(text, pattern, position):
            match_positions.append(position)
    print(" ".join(map(str, match_positions[::-1])))