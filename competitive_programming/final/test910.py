import math
import typing
import unittest


class Task(typing.NamedTuple):

    duration: int
    last_start: int


def read_tasks(filename: str) -> typing.List[Task]:
    def create_task(line: str) -> Task:
        [duration, last_start] = list(map(int, line.split()))
        return Task(duration, last_start)
    with open(filename, 'r') as source:
        n = int(source.readline())
        return list(map(lambda _: create_task(source.readline()), range(n)))


def calc_optimal_schedule(tasks: typing.List[Task]) -> int:
    dest = [[math.inf for _ in range(len(tasks) + 1)] for _ in range(len(tasks) + 1)]
    dest[0][0] = 0
    for task_index in range(len(tasks)):
        for tasks_count in range(len(tasks) + 1):
            if dest[task_index][tasks_count] != math.inf:
                dest[task_index + 1][tasks_count] = min(dest[task_index + 1][tasks_count], dest[task_index][tasks_count])
                if dest[task_index][tasks_count] <= tasks[task_index].last_start:
                    dest[task_index + 1][tasks_count + 1] = min(dest[task_index + 1][tasks_count + 1], dest[task_index][tasks_count] + tasks[task_index].duration)
    for tasks_count in range(len(tasks), -1, -1):
        if dest[len(tasks)][tasks_count] != math.inf:
            return tasks_count


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        tasks = [Task(8, 25), Task(5, 12), Task(7, 10), Task(11, 28), Task(3, 18), Task(6, 32), Task(10, 45), Task(5, 34), Task(7, 28), Task(6, 42)]
        self.assertEqual(7, calc_optimal_schedule(tasks))

    def test_task1(self):
        tasks = read_tasks("./time.in")
        self.assertEqual(10, calc_optimal_schedule(tasks))

    def test_task2(self):
        tasks = read_tasks("./time2.in")
        self.assertEqual(38, calc_optimal_schedule(tasks))


if __name__ == "__main__":
    unittest.main()