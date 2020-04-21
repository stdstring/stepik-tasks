import typing


class DisjointSetElementData(typing.NamedTuple):
    parent: int
    size: int


def get_head(variables: typing.List[DisjointSetElementData], number: int) -> DisjointSetElementData:
    element = variables[number - 1]
    if element.parent == number:
        return element
    head = get_head(variables, element.parent)
    variables[number - 1] = DisjointSetElementData(head.parent, element.size)
    return head


def union(variables: typing.List[DisjointSetElementData], number_i: int, number_j: int) -> None:
    head_i = get_head(variables, number_i)
    head_j = get_head(variables, number_j)
    if head_i.parent == head_j.parent:
        return
    if head_i.size < head_j.size:
        variables[head_i.parent - 1] = DisjointSetElementData(head_j.parent, 0)
        variables[head_j.parent - 1] = DisjointSetElementData(head_j.parent, head_i.size + head_j.size)
    else:
        variables[head_i.parent - 1] = DisjointSetElementData(head_i.parent, head_i.size + head_j.size)
        variables[head_j.parent - 1] = DisjointSetElementData(head_i.parent, 0)


def process_equalities(variables: typing.List[DisjointSetElementData], count: int) -> None:
    for _ in range(count):
        [variable_i, variable_j] = list(map(int, input().split()))
        union(variables, variable_i, variable_j)


def process_inequalities(variables: typing.List[DisjointSetElementData], count: int) -> bool:
    for _ in range(count):
        [variable_i, variable_j] = list(map(int, input().split()))
        head_i = get_head(variables, variable_i)
        head_j = get_head(variables, variable_j)
        if head_i.parent == head_j.parent:
            return False
    return True


if __name__ == "__main__":
    [n, e, d] = list(map(int, input().split()))
    variables = [DisjointSetElementData(number, 1) for number in range(1, n + 1)]
    process_equalities(variables, e)
    print("1" if process_inequalities(variables, d) else "0")
