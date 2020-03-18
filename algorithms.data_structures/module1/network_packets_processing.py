import collections


def process() -> None:
    size, n = map(int, input().split())
    packets = map(lambda _: map(int, input().split()), range(n))
    times_queue = collections.deque()
    for arrival, duration in packets:
        while len(times_queue) > 0 and times_queue[0] <= arrival:
            times_queue.popleft()
        if len(times_queue) < size:
            start_time = arrival if len(times_queue) == 0 else times_queue[-1]
            print(start_time)
            times_queue.append(start_time + duration)
        else:
            print(-1)


if __name__ == "__main__":
    process()