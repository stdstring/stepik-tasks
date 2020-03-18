import collections


def process() -> None:
    n = int(input())
    source = list(map(int, input().split()))
    m = int(input())
    max_queue = collections.deque()
    dest = []
    # init max_queue
    for index in range(m):
        while (len(max_queue) > 0) and (max_queue[-1] < source[index]):
            max_queue.pop()
        max_queue.append(source[index])
    dest.append(max_queue[0])
    # process other elements
    for index in range(m, n):
        if source[index - m] == max_queue[0]:
            max_queue.popleft()
        while (len(max_queue) > 0) and (max_queue[-1] < source[index]):
            max_queue.pop()
        max_queue.append(source[index])
        dest.append(max_queue[0])
    print (" ".join(map(str, dest)))


if __name__ == "__main__":
    process()