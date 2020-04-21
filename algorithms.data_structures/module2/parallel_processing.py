from queue import PriorityQueue
import typing


class Task(typing.NamedTuple):
    finish_time: int
    processor: int


if __name__ == "__main__":
    [n, m] = list(map(int, input().split()))
    task_times = list(map(int, input().split()))
    priority_queue = PriorityQueue(n)
    init_size = n if n <= m else m
    for number in range(init_size):
        print(f"{number} 0")
        priority_queue.put(Task(task_times[number], number))
    for index in range(init_size, m):
        processed_task = priority_queue.get()
        print(f"{processed_task.processor} {processed_task.finish_time}")
        priority_queue.put(Task(processed_task.finish_time + task_times[index], processed_task.processor))
