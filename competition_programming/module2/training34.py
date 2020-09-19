import typing
import unittest


class Order(typing.NamedTuple):

    deadline: int
    cost: int


def read_order_list(filename: str) -> typing.List[Order]:
    def create_order(line: str) -> Order:
        [deadline, cost] = list(map(int, line.split()))
        return Order(deadline, cost)
    with open(filename, 'r') as source:
        n = int(source.readline())
        return list(map(lambda _: create_order(source.readline()), range(n)))


def calc_max_total_cost(orders: typing.List[Order]) -> int:
    orders = sorted(orders, key=lambda order: order.cost, reverse=True)
    max_deadline = max(orders, key=lambda order: order.deadline).deadline
    used = (max_deadline + 1) * [False]
    total_cost = 0
    for order in orders:
        deadline = order.deadline
        while (deadline >= 1) and (used[deadline]):
            deadline -= 1
        if deadline > 0:
            used[deadline] = True
            total_cost += order.cost
    return total_cost


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        orders = [Order(2, 5), Order(2, 4), Order(5, 3), Order(1, 2), Order(3, 1)]
        self.assertEqual(13, calc_max_total_cost(orders))

    def test_task1(self):
        orders = read_order_list("./schedule.in")
        self.assertEqual(374, calc_max_total_cost(orders))

    def test_task2(self):
        orders = read_order_list("./schedule2.in")
        self.assertEqual(2305658251934, calc_max_total_cost(orders))


if __name__ == "__main__":
    unittest.main()
