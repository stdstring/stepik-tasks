import typing
import unittest


class InputData(typing.NamedTuple):

    duration: int
    tasks: typing.List[int]


class TasksResult(typing.NamedTuple):

    count: int
    penalty_time: int


def read_input_data(filename: str) -> InputData:
    with open(filename, 'r') as source:
        [_, duration] = list(map(int, source.readline().split()))
        tasks = list(map(int, source.readline().split()))
        return InputData(duration, tasks)


def calc_best_tasks_result(input_data: InputData) -> TasksResult:
    tasks = sorted(input_data.tasks)
    tasks_count = 0
    tasks_penalty_time = 0
    current_time = 0
    task_index = 0
    while (current_time < input_data.duration) and (task_index < len(tasks)):
        if tasks[task_index] > (input_data.duration - current_time):
            return TasksResult(tasks_count, tasks_penalty_time)
        tasks_count += 1
        current_time += tasks[task_index]
        tasks_penalty_time += current_time
        task_index += 1
    return TasksResult(tasks_count, tasks_penalty_time)


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        input_data = InputData(60, [30, 40, 20])
        self.assertEqual(TasksResult(2, 70), calc_best_tasks_result(input_data))

    def test_task(self):
        input_data = read_input_data("./contest.in")
        self.assertEqual(TasksResult(446, 7302802), calc_best_tasks_result(input_data))


if __name__ == "__main__":
    unittest.main()