import typing


p = 1000000007
x = 263
max_size = 15


def calc_x_powers() -> typing.List[int]:
    x_powers = [1]
    for power in range(1, max_size):
        x_powers.append((x_powers[power - 1] * x) % p)
    return x_powers


x_powers = calc_x_powers()


def calc_hash(source: str, m: int) -> int:
    result = 0
    for (power, ch) in enumerate(source):
        result += (ord(ch) * x_powers[power]) % p
        result = result % p
    return result % m


class Chain:

    def __init__(self, value: typing.Any, next_item: 'Chain'):
        self.value = value
        self.next_item = next_item


def has_value_in_chain(chain_head: Chain, value: str) -> bool:
    current = chain_head
    while current is not None:
        if current.value == value:
            return True
        current = current.next_item
    return False


def chain_to_list(chain_head: Chain) -> typing.List[str]:
    dest = []
    current = chain_head
    while current is not None:
        dest.append(current.value)
        current = current.next_item
    return dest


def del_value_from_chain(chain_head: Chain, value: str) -> Chain:
    parent = None
    current = chain_head
    while current is not None:
        if current.value == value:
            if parent is None:
                return current.next_item
            else:
                parent.next_item = current.next_item
                return chain_head
        parent = current
        current = current.next_item
    return chain_head


if __name__ == "__main__":
    m = int(input())
    hash_table = [None for _ in range(m)]
    n = int(input())
    for _ in range(n):
        request = input().split()
        method = request[0]
        if method == "add":
            hash_value = calc_hash(request[1], m)
            if not has_value_in_chain(hash_table[hash_value], request[1]):
                hash_table[hash_value] = Chain(request[1], hash_table[hash_value])
        elif method == "del":
            hash_value = calc_hash(request[1], m)
            hash_table[hash_value] = del_value_from_chain(hash_table[hash_value], request[1])
        elif method == "find":
            hash_value = calc_hash(request[1], m)
            print("yes" if has_value_in_chain(hash_table[hash_value], request[1]) else "no")
        elif method == "check":
            print(" ".join(chain_to_list(hash_table[int(request[1])])))